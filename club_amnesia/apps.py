from django.contrib.admin.apps import AdminConfig

class MyClubAdminConfig(AdminConfig):
    default_site = 'club_amnesia.admin.MyClubAdmin'