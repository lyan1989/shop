from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Bitfunx'
    site_title = 'Bitfunx Manager'
    index_title = 'HOME'


custom_site = CustomSite(name='cus_admin')

