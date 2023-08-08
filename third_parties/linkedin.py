import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkeIn profile
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    return response
