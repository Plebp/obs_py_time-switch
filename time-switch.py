import obspython as obs
import time

interval = 0
interval_bak = 0

def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(props, "interval", "Interval (Minuten)", 2, 1500, 1)
    obs.obs_properties_add_bool(props, "enabled", "Aktiviert")
    return props

def script_load(settings):
    print("Script geladen.")
    
def script_description():
    return "<b> TIMER </b>" + \
           "<br/>" + \
           "<br/>" + \
           "Schaltet den Stream im Interval ein/aus."

def script_update(settings):
    global interval
    global interval_bak
    obs.timer_remove(decrease_interval)
    if obs.obs_data_get_bool(settings, "enabled"):
        interval = obs.obs_data_get_int(settings, "interval") - 1
        interval_bak = interval
        print("Timer aktiviert [" + str(interval + 1) + "min]")
        if interval > 0:
            obs.timer_add(decrease_interval, 1000 * 60)
    else:
        print("Timer deaktiviert")

def startStream():
    obs.obs_frontend_streaming_start()
    print("Stream gestartet")

def stopStream():
    obs.obs_frontend_streaming_stop()
    print("Stream gestoppt")

def decrease_interval():
    global interval
    global interval_bak
    if interval > 0:
        print("Aktueller Loop: " + str(interval) + " Minuten übrig.")
        interval = interval - 1
    else:
        if obs.obs_frontend_streaming_active():
            stopStream()
        else:
            startStream()
        interval = interval_bak


        
