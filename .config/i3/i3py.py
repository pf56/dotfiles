import i3pystatus

status = i3pystatus.core.Status()

status.register("clock", format="  %a %F  %T",)

status.register("pulseaudio", format=" {volume}", multi_colors=True)

status.register("load", format="{avg5} {avg1}")

status.register("cpu_usage")

status.register("temp")

status.register("network", interface="enp0s25",
                format_up=" {bytes_sent} MiB/s  {bytes_recv} MiB/s",
                divisor=1024**2)

status.register("disk", format=" {avail} GiB",
                path="/")

status.register("weather", location_code="GMXX0063", colorize=True,
                format="{current_temp}")

status.register("spotify", format=" {status} {artist} - {title}",
                format_not_running="")

status.run()
