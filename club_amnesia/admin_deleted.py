from django.contrib.admin import AdminSite

class MyClubAdmin(AdminSite):
    site_header = 'Custom Administration'
    site_title = 'Custom Site Admin'
    index_title = 'Custom Site Admin Home'