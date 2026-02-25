test_settings = {
    'theme': 'light',
    'language': 'english',
    'notifications': 'enabled'
}

def add_setting(settings_dict,settings):
    key,value=settings
    key=key.lower()
    value=value.lower()
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict,setting):
    key,value=setting
    key=key.lower()
    value=value.lower()
    if key in settings_dict:
        settings_dict[key]=value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict,key):
    key=key.lower()
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return"No settings available."

    result="settings are:\n"
    for key,value in settings_dict.items():
        result+= f"{key.capitalize()} : {value}\n"
    return result


print(update_setting(test_settings, ('Theme', 'Dark')))

