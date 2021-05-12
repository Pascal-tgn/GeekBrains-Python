class Inventory:
    devices: dict

    def __init__(self, devices={'Printer': 0, 'Scanner': 0, 'Xerox': 0}):
        self.devices = devices

    def provide(self, device, department):
        if self.devices[device.__class__.__name__] > 0:
            self.devices[device.__class__.__name__] -= 1
            device.department = department
        else:
            print("No devices in stock!")

    def add(self, *args):
        for device in args:
            if device.department == 'In stock':
                print('Device already in stock!')
            else:
                self.devices[device.__class__.__name__] += 1
                device.department = 'In stock'


class OfficeEquipment:
    paperType: str
    ppm: int
    dimensions: str
    ppi: int
    inventoryNumber: str
    department: str

    def __init__(self, inventoryNumber, paperType='A4', ppm=18, dimensions='Not defined', ppi=300,
                 department='Unassigned'):
        self.inventoryNumber = inventoryNumber
        self.paperType = paperType
        self.ppm = ppm
        self.dimensions = dimensions
        self.ppi = ppi
        self.department = department


class Printer(OfficeEquipment):
    interfaces: list
    tonerType: str
    colorMode: str

    def __init__(self, interfaces, tonerType, colorMode, *args, **kwargs):
        self.interfaces = interfaces
        self.tonerType = tonerType
        self.colorMode = colorMode
        super(Printer, self).__init__(**kwargs)


class Scanner(OfficeEquipment):
    interfaces: list
    feederType: str
    outputFormats: str

    def __init__(self, interfaces, feederType='flatbed', outputFormats='JPG, PDF', *args, **kwargs):
        self.interfaces = interfaces
        self.feederType = feederType
        self.outputFormats = outputFormats
        super(Scanner, self).__init__(**kwargs)


class Xerox(OfficeEquipment):
    feederType: str

    def __init__(self, feederType, *args, **kwargs):
        self.feederType = feederType
        super(Xerox, self).__init__(**kwargs)


storage = Inventory()
printer1 = Printer(inventoryNumber='CY0001267', interfaces=('USB', 'LAN', 'WiFi'), tonerType='dry', colorMode='CMYK')
scanner1 = Scanner(inventoryNumber='CY0001245', interfaces='USB')
xerox1 = Xerox(inventoryNumber='CY0002317', feederType='Automatic')
storage.add(printer1, scanner1, xerox1)
storage.provide(printer1, 'Accounting')
print(f"Printer with inventory number {printer1.inventoryNumber} assigned to {printer1.department}")
print(f"Devices in stock: {storage.devices}")
