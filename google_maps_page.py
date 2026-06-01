from playwright.sync_api import Page, expect

class GoogleMapsPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.get_by_role("combobox", name="Search Google Maps")
        self.search_button = page.get_by_role("button", name="Search")
        self.results_heading = page.get_by_role("heading", name="Results")
        self.result_cards = page.locator("div[role='article']")

    def navigate_using_coordinates(self, lat: float, lng: float):
        print(f"Navigating to coordinates: {lat}, {lng}...")
        self.page.goto(f"http://www.google.com/maps/@{lat},{lng},15z")

    def navigate_without_coordinates(self):
        print("Navigating to www.google.com/maps...")
        self.page.goto("http://www.google.com/maps")

    def verify_page_load(self):
        expect(self.page).to_have_title("Google Maps")
        expect(self.search_box).to_be_visible()
        expect(self.search_button).to_be_visible()

    def do_search(self, term: str):
        print(f"Searching for '{term}'...")
        self.search_box.fill(term)
        self.search_button.click()

    def verify_results_displayed(self):
        print("Verifying results appeared...")
        expect(self.results_heading).to_be_visible()
        expect(self.result_cards.first).to_be_visible()

    def has_category_in_results(self, category_keyword: str) -> bool:
        card_count = self.result_cards.count()
        print(f"Scanning {card_count} loaded cards for category keyword: '{category_keyword}'")
        
        for i in range(card_count):
            card_text = self.result_cards.nth(i).inner_text()
            if category_keyword in card_text:
                business_name = card_text.split("\n")[0]
                print(f"FOUND MATCH: '{business_name}' contains target category at results list position {i+1}.")
                print(f"Full result details: {card_text}")
                return True
        return False