import os
import sys
import requests
import numpy as np
from numpy import array as np_array

class TBAParser:
    def __init__(self, teamNumber, packageID, versionID):
        self.teamNumber = teamNumber
        self.packageID = packageID
        self.versionID = versionID
        self.header = {'X-TBA-App-Id': 'frc{team}:{package}:{version}'.format(team = teamNumber, package = packageID, version = versionID)}
        self.baseURL = 'http://www.thebluealliance.com/api/v2'

    #Team Info

    def __get_list_by_page(self, page):
        request = (self.baseURL + "/teams/" + str(page))
        response = requests.get(request, headers = self.header)
        response_list = response.json()
        return response_list

    def __get_last_team_list(self): #Class Function, brute-forces the last page of teams
        checkpage = 0

        for page in range(0,100): #Plenty of room for team expansion, up to 55000 teams.  API will probably be on v3 or greater by then.
            content = self.get_team_list_obj(page)
            try:
                if not content[0] is None:
                    checkpage += 1
                else:
                    return checkpage
            except:
                return checkpage

    def get_team_list_obj(self, page=None):
        if page:
            full_list = self.__get_list_by_page(page)
        else:
            lastpage = self.__get_last_team_list()
            full_list = []

            for page in range(0, lastpage): #From first page to calculated last page through self.__get_last_team_list
                partial_list = self.get_team_list_obj(page)
                full_list = full_list + partial_list #combine partial with previously set up 'full' list to grow list as we iterate over the range of pages

            return full_list

    def get_team_obj(self, team_number): #get the full 'team' object for the given team number
        request = (self.baseURL + "/team/frc" + str(team_number))
        response = requests.get(request, headers = self.header)
        dictionary = response.json()
        return dictionary

    def get_team_full_name(self, team_number): #pull full name out of team obj
        team_dictionary = self.get_team_obj(team_number)
        full_name = team_dictionary['name']
        return full_name

    def get_team_nick_name(self, team_number): #pull nickname out of team obj
        team_dictionary = self.get_team_obj(team_number)
        nick_name = team_dictionary['nickname']
        return nick_name

    def get_team_number(self, team_number): #pull team number out of team obj
        team_dictionary = self.get_team_obj(team_number)
        team_number = team_dictionary['team_number']
        return team_number

    def get_team_rookie_year(self, team_number): #pull team's rookie year out of team obj
        team_dictionary = self.get_team_obj(team_number)
        rookie_year = team_dictionary['rookie_year']
        return rookie_year

    def get_team_website(self, team_number): #pull team website url out of team obj
        team_dictionary = self.get_team_obj(team_number)
        website = team_dictionary['website']
        return website

    def get_team_city(self, team_number): #pull the team's city out of team obj
        team_dictionary = self.get_team_obj(team_number)
        city = team_dictionary['locality']
        return city

    def get_team_region(self, team_number): #pull the team's state / region out of team obj
        team_dictionary = self.get_team_obj(team_number)
        region = team_dictionary['region']
        return region

    def get_team_location(self, team_number): #pull team's full stylized location out of team obj
        team_dictionary = self.get_team_obj(team_number)
        location = team_dictionary['location']
        return location

    def get_team_key(self, team_number): #pull the team's API refrence key out of team obj
        team_dictionary = self.get_team_obj(team_number)
        key = team_dictionary['key']
        return key

    def get_team_country(self, team_number): #pull the team's country of origin out of team obj
        team_dictionary = self.get_team_obj(team_number)
        country = team_dictionary['country_name']
        return country

    def get_team_motto(self, team_number): #pull team motto out of team obj
        team_dictionary = self.get_team_obj(team_number)
        motto = team_dictionary['motto']
        return motto


    #Event Info

    def get_event_obj(self, eventKey):
        request = (self.baseURL + "/event/" + eventKey)
        response = requests.get(request, headers = self.header)
        dictionary = response.json()
        return dictionary

    def get_event_key(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_key = event_dictionary['key']
        return event_key

    def get_event_website(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_website = event_dictionary['website']
        return event_website

    def get_event_is_official(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_is_official = event_dictionary['official']
        return event_is_official

    def get_event_end_date(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_end_date = event_dictionary['end_date']
        return event_end_date

    def get_event_name(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_name = event_dictionary['name']
        return event_name

    def get_event_short_name(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_short_name = event_dictionary['short_name']
        return event_short_name

    def get_event_facebook_eid(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_facebook_eid = event_dictionary['facebook_eid']
        return event_facebook_eid

    def get_event_district_string(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_district_string = event_dictionary['event_district_string']
        return event_district_string

    def get_event_venue_address(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_venue_address = event_dictionary['venue_address']
        return event_venue_address

    def get_event_district(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_district = event_dictionary['event_district']
        return event_district

    def get_event_location(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_location = event_dictionary['location']
        return event_location

    def get_event_code(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_code = event_dictionary['event_code']
        return event_code

    def get_event_year(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_year = event_dictionary['year']
        return event_year

    def get_event_webcast(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_webcast = event_dictionary['webcast']
        return event_webcast

    def get_event_timezone(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_timezone = event_dictionary['timezone']
        return event_timezone

    def get_event_alliances(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_alliances = event_dictionary['alliances']
        return event_alliances

    def get_event_alliance(self, eventKey, number):
        event_dictionary = self.get_event_obj(eventKey)
        event_alliance = event_dictionary['alliances'][number - 1]
        return event_alliance

    def get_event_alliance_members(self, eventKey, number):
        event_dictionary = self.get_event_obj(eventKey)
        event_alliance_picks = event_dictionary['alliances'][number - 1]['picks']
        return event_alliance_picks

    def get_event_alliance_declines(self, eventKey, number):
        event_dictionary = self.get_event_obj(eventKey)
        event_alliance_declines = event_dictionary['alliances'][number - 1]['declines']
        return event_alliance_declines

    def get_event_type_string(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_type_string = event_dictionary['event_type_string']
        return event_type_string

    def get_event_start_date(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_start_date = event_dictionary['start_date']
        return event_start_date

    def get_event_event_type(self, eventKey):
        event_dictionary = self.get_event_obj(eventKey)
        event_event_type = event_dictionary['event_type']
        return event_event_type
