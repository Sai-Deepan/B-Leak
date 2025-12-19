# Sai

# Sai

import asyncio
from bleak import BleakScanner

def callback(device, advertisement_data):
    print({
        "mac": device.address,
        "name": device.name,
        "rssi": advertisement_data.rssi,
        "tx_power": advertisement_data.tx_power,
        "services": advertisement_data.service_uuids,
        "manufacturer": advertisement_data.manufacturer_data
    })

scanner = BleakScanner(callback)


async def main():
    scanner = BleakScanner(callback)
    await scanner.start()
    print("Live scan started")
    await asyncio.sleep(15)
    await scanner.stop()
    print("Scan stopped")

asyncio.run(main())

# Repeating the same device multiple times
# Not a structured format
# Need more data
