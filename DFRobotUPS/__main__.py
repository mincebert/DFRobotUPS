# DFRobotUPS.__main__.py



from DFRobotUPS import DFRobotUPS



if __name__ == "__main__":
    ups = DFRobotUPS()

    print("Product ID = 0x%x" % ups.pid)
    print("Firmware version = %d.%d" % ups.fwver)
    print("Battery voltage = %dmV" % ups.vcell)
    print("State of Charge = %.2f%%" % ups.soc)
