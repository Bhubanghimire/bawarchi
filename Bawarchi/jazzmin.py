JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Bawarchi Food Cafe',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Bawarchi',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # 'site_logo': 'img/logo/logo.png',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Admin panel',

    # Copyright on the footer
    'copyright': 'photo',

    # The model admin to search from the search bar, search bar omitted if excluded
    # 'search_model': 'properties.Property',

    # Field name on user model that contains avatar image
    'user_avatar': "profile",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home', 'url': '/',
         'permissions': ['auth.view_user']},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},
        {'app': 'properties'},

        # App with dropdown menu to all its models pages (Permissions checked against models)

    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
        {'model': 'auth.user'},
        {'name': 'Support', 'url': 'https://github.com/Bhubanghimire',
         'new_window': True},
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps to base side menu ordering off of (does not need to contain all apps)
    # 'order_with_respect_to': ['accounts', 'polls'],

    # Custom links to append to app groups, keyed on app name

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes

    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },
    # 'custom_css': 'css/admin.css',
    #  "show_ui_builder": True,

}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-danger navbar-dark",
    "no_navbar_border": False,
    "sidebar": "sidebar-dark-danger",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}