from i3pystatus import Status
from i3pystatus.weather import weathercom
from i3pystatus import parcel

import config

status = Status()

status.register("clock", format="  %a %F  %T",)

status.register("dpms", format="", format_disabled="", color_disabled="#A52A2A")

status.register("pulseaudio", format=" {volume}", multi_colors=True)

status.register("load", format="{avg5} {avg1}")

status.register("cpu_usage")

status.register("temp")

status.register("network", interface="enp0s25",
                format_up=" {bytes_sent} MiB/s  {bytes_recv} MiB/s",
                divisor=1024**2, recv_limit=100000, sent_limit=40000)

#status.register("xkblayout", layouts=["de", "us colemak"])

status.register("disk", format=" {avail} GiB",
                path="/")

status.register("weather", backend=weathercom.Weathercom(location_code="GMXX4347:1:GM", units="metric"), colorize=True,
                format="{current_temp}°C")

status.register("spotify", format=" {status} {artist} - {title}")

#status.register("sabnzbd", host="10.0.10.21",
#                api_key=config.sabnzbd_api)

status.run()
