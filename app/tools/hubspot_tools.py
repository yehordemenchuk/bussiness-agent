from langchain_core.tools import tool

from app.tools import call_api
from app.config import Config

@tool
def create_lead(firstname: str = None, lastname: str = None, email: str = None,
                phone: str = None, company: str = None):
    """Create a lead in the CRM system."""
    return call_api("https://api.hubapi.com/crm/v3/objects/contacts", "POST",
                 {"Authorization": f"Bearer {Config.HUBSPOT_API_KEY}"},
                   {"properties": form_lead_properties(firstname = firstname,
                                                          lastname = lastname, email = email,
                                                          phone = phone, company = company)
                        })

def form_lead_properties(**kwargs) -> dict:
    properties = {}

    for key in kwargs:
        if kwargs[key]:
            properties[key] = kwargs[key]

    return properties