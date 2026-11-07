print("-----------Welcome to the QUIZ GAME-----------")

playing_input = input("Do you want to play? ")

if playing_input.lower() != "yes":
    quit()

print("-----------Okay! Let's Play :)-----------")
score = 0

questions = {
    "What does AI stand for?": "artificial intelligence",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit",
    "What does CPU stand for?": "central processing unit",
    "What does SSD stand for?": "solid state drive",
    "What does USB stand for?": "universal serial bus",
    "What does LAN stand for?": "local area network",
    "What does HTML stand for?": "hypertext markup language",
    "What does DNS stand for?": "domain name system",
    "What does IP stand for?": "internet protocol",
    "What does HTTP stand for?": "hypertext transfer protocol",
    "What does HTTPS stand for?": "hypertext transfer protocol secure",
    "What does URL stand for?": "uniform resource locator",
    "What does FTP stand for?": "file transfer protocol",
    "What does VPN stand for?": "virtual private network",
    "What does API stand for?": "application programming interface",
    "What does IDE stand for?": "integrated development environment",
    "What does OS stand for?": "operating system",
    "What does UI stand for?": "user interface",
    "What does UX stand for?": "user experience",
    "What does SQL stand for?": "structured query language",
    "What does JSON stand for?": "javascript object notation",
    "What does XML stand for?": "extensible markup language",
    "What does CSS stand for?": "cascading style sheets",
    "What does CLI stand for?": "command line interface",
    "What does GUI stand for?": "graphical user interface",
    "What does CRT stand for?": "cathode ray tube",
    "What does LCD stand for?": "liquid crystal display",
    "What does LED stand for?": "light emitting diode",
    "What does ROM stand for?": "read only memory",
    "What does BIOS stand for?": "basic input output system",
    "What does HDMI stand for?": "high definition multimedia interface",
    "What does VGA stand for?": "video graphics array",
    "What does Wi-Fi stand for?": "wireless fidelity",
    "What does ISP stand for?": "internet service provider",
    "What does WWW stand for?": "world wide web",
    "What does ERP stand for?": "enterprise resource planning",
    "What does CRM stand for?": "customer relationship management",
    "What does SaaS stand for?": "software as a service",
    "What does IoT stand for?": "internet of things",
    "What does PDF stand for?": "portable document format",
    "What does JPEG stand for?": "joint photographic experts group",
    "What does PNG stand for?": "portable network graphics",
    "What does GIF stand for?": "graphics interchange format",
    "What does CSV stand for?": "comma separated values",
    "What does ASCII stand for?": "american standard code for information interchange",
    "What does MIME stand for?": "multipurpose internet mail extensions",
    "What does SMTP stand for?": "simple mail transfer protocol",
    "What does POP stand for?": "post office protocol",
    "What does IMAP stand for?": "internet message access protocol",
    "What does DHCP stand for?": "dynamic host configuration protocol",
    "What does NAT stand for?": "network address translation",
    "What does TCP stand for?": "transmission control protocol",
    "What does UDP stand for?": "user datagram protocol",
    "What does SSH stand for?": "secure shell",
    "What does TLS stand for?": "transport layer security",
    "What does SSL stand for?": "secure sockets layer",
    "What does MAC stand for?": "media access control",
    "What does NIC stand for?": "network interface card",
    "What does HDD stand for?": "hard disk drive",
    "What does CD-ROM stand for?": "compact disc read only memory",
    "What does DVD stand for?": "digital versatile disc",
    "What does OCR stand for?": "optical character recognition",
    "What does QR stand for?": "quick response",
    "What does RFID stand for?": "radio frequency identification",
    "What does GPS stand for?": "global positioning system",
    "What does UPS stand for?": "uninterruptible power supply",
    "What does ATM stand for?": "automated teller machine",
    "What does POS stand for?": "point of sale",
    "What does PIN stand for?": "personal identification number",
    "What does NFC stand for?": "near field communication",
    "What does USB-C stand for?": "universal serial bus type c",
    "What does RAID stand for?": "redundant array of independent disks",
    "What does SAN stand for?": "storage area network",
    "What does NAS stand for?": "network attached storage",
    "What does VPN stand for in networking?": "virtual private network",
    "What does CMS stand for?": "content management system",
    "What does CDN stand for?": "content delivery network",
    "What does PaaS stand for?": "platform as a service",
    "What does IaaS stand for?": "infrastructure as a service",
    "What does DevOps stand for?": "development and operations",
    "What does CI stand for?": "continuous integration",
    "What does CD stand for?": "continuous delivery",
    "What does QA stand for?": "quality assurance",
    "What does MVP stand for?": "minimum viable product",
    "What does SDK stand for?": "software development kit",
    "What does DNS stand for on the internet?": "domain name system",
    "What does OOP stand for?": "object oriented programming",
    "What does UML stand for?": "unified modeling language",
    "What does REST stand for?": "representational state transfer",
    "What does CRUD stand for?": "create read update delete",
    "What does IDE stand for in programming?": "integrated development environment",
    "What does Git stand for?": "global information tracker",
    "What does SSH stand for in secure access?": "secure shell",
    "What does XSS stand for?": "cross site scripting",
    "What does CSRF stand for?": "cross site request forgery",
    "What does SQL stand for in databases?": "structured query language",
    "What does CPU stand for in computing?": "central processing unit",
    "What does OS stand for in computing?": "operating system",
}

for question, correct_answer in questions.items():
    answer = input(question + " ").lower().strip()

    if answer == correct_answer:
        print("-----------Correct-----------")
        score += 1
    elif answer == "q":
        print("-----------You quit the game-----------")
        break
    else:
        print(f"-----------Wrong. The answer is {correct_answer}-----------")

percentage = (score / len(questions)) * 100
print(f"You got {score} question(s) correct!")
print(f"You got {percentage:.0f}% of the questions correct")