#!/usr/bin/env python
# encoding: utf-8

"""
tests.py

Unit tests for crunchbase API library.
"""

import unittest
import simplejson

from crunchbase import crunchbase

class TestCrunchbase(unittest.TestCase):
    # known resources
    COMPANY = "techcrunch"
    PERSON_FIRST_NAME = "michael"
    PERSON_LAST_NAME = "arrington"
    FINANCIAL_ORG = "sequoia-capital"
    PRODUCT = "crunchbase"
    SERVICE_PROVIDER = "verisign"
    
    api = crunchbase()
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_get_company_data(self):
        """Grab company data and make sure it's non-empty and JSON"""
        json = self.api.getCompanyData(self.COMPANY)
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_get_person_data(self):
        """Grab person data and make sure it's non-empty and JSON"""
        json = self.api.getPersonData(self.PERSON_FIRST_NAME, self.PERSON_LAST_NAME)
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_get_financial_org_data(self):
        """Grab financial org data and make sure it's non-empty and JSON"""
        json = self.api.getFinancialOrgData(self.FINANCIAL_ORG)
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_get_product_data(self):
        """Grab product data and make sure it's non-empty and JSON"""
        json = self.api.getProductData(self.PRODUCT)
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_get_service_provider_data(self):
        """Grab service provider data and make sure it's non-empty and JSON"""
        json = self.api.getServiceProviderData(self.SERVICE_PROVIDER)
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_list_companies(self):
        """Grab list of companies and make sure it's non-empty and JSON"""
        json = self.api.listCompanies()
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_list_people(self):
        """Grab list of people and make sure it's non-empty and JSON"""
        json = self.api.listPeople()
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_list_financial_orgs(self):
        """Grab list of financial orgs and make sure it's non-empty and 
        JSON"""
        json = self.api.listFinancialOrgs()
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_list_products(self):
        """Grab list of products and make sure it's non-empty and JSON"""
        json = self.api.listProducts()
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
    def test_list_service_providers(self):
        """Grab list of service providers and make sure it's non-empty and 
        JSON"""
        json = self.api.listServiceProviders()
        self.assertNotEqual(json, "")
        simplejson.loads(json)
        return True
        
if __name__ == '__main__':
    unittest.main()
    