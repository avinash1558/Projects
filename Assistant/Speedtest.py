

import speedtest


def Speedtesting():
    try:
        sp = speedtest.Speedtest()
        sp.get_servers()
        down = str(round(sp.download()/(10**6), 3))+" Mbps"
        up = str(round(sp.upload()/(10**6), 3))+" Mbps"
        speed = f"Download Speed : {down} And Upload Speed {up}"

        return speed
    except:
        return "An unknown error occurred, Sorry sir try again"
