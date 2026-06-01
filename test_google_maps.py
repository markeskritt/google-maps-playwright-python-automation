#from playwright.sync_api import sync_playwright
import pytest
from google_maps_page import GoogleMapsPage 

@pytest.fixture
def maps_page(context):
    context.grant_permissions(["geolocation"])
    
    page = context.new_page()
    
    # Initialize and return the Page Object Model
    return GoogleMapsPage(page)

# TEST CASE 1: Feeding in a geo-location for a reliable Toronto Midtown Search
def test_search_with_coordinates(maps_page):
    """searching with data driven coordinates for Toronto Midtown"""
    latitude = 43.7067
    longitude = -79.3984
    
    maps_page.navigate_using_coordinates(latitude, longitude)
    maps_page.verify_page_load()
    
    maps_page.do_search("restaurants")
    maps_page.verify_results_displayed()
    
    # verify a restaurant result is returned
    assert maps_page.has_category_in_results("Restaurant")

# 3. TEST CASE 2: The Local Location SEARCH
def test_search_without_coordinates(maps_page):
    """Searching without coordinates, using local location."""
    
    maps_page.navigate_without_coordinates()
    maps_page.verify_page_load()
    
    maps_page.do_search("restaurants")
    maps_page.verify_results_displayed()
    
    # verify a restaurant result is returned
    assert maps_page.has_category_in_results("Restaurant")
