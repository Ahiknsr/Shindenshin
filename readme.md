 
# About:

[Shindenshin](https://github.com/Ahiknsr/Shindenshin) allows you to send push notifications to your ios/android devices from *nix shell.

# Setup

* Vist [Microsoft Flow](https://flow.microsoft.com) and use the http_push_notification_flow.json file in this repo as a template to create a new flow
* Once the flow is created save the url generated for flow in .flow_urls file in your home direcory.
* Install the Microsoft Flow app on your mobile device and sign-in

# Usage

`python2 main.py -c "aria2c http://mirror.cse.iitk.ac.in/archlinux/iso/2017.12.01/archlinux-bootstrap-2017.12.01-x86_64.tar.gz"`

will send a push notification to your mobile device once the download is completed


# But why?
I was looking for a app which would allow me to send push notifications to my ios device using a http endpoint. I found few apps but they are either paid or have limits on number of notifications that can be sent , after some searching i found Microsoft Flow and wrote this script as a wrapper to use this.
