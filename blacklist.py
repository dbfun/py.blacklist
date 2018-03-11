# -*- coding: utf-8 -*-

"""
209.85.161.176 - пример IP адреса, у которого dnsbl.sorbs.net Low Risk

curl 'http://www.ip-score.com/ajax_handler/get_bls' --data 'ip=209.85.161.176&server=dnsbl.sorbs.net'
Ответ: {"dnsbl.sorbs.net":"127.0.0.6"}
"""

# requests: @see http://docs.python-requests.org/en/master/user/quickstart/
import requests, sys


# API, через который происходит проверка
url = 'http://www.ip-score.com/ajax_handler/get_bls'

# Проверяемый IP адрес
ip='209.85.161.176'

# Список серверов с блек-листами
blacklist = [
  'access.redhawk.org', 'b.barracudacentral.org', 'bl.shlink.org', 'bl.spamcannibal.org',
  'bl.spamcop.net', 'bl.tiopan.com', 'blackholes.wirehub.net', 'blacklist.sci.kun.nl',
  'block.dnsbl.sorbs.net', 'blocked.hilli.dk', 'bogons.cymru.com', 'cart00ney.surriel.com',
  'cbl.abuseat.org', 'cblless.anti-spam.org.cn', 'dev.null.dk', 'dialup.blacklist.jippg.org',
  'dialups.mail-abuse.org', 'dialups.visi.com', 'dnsbl.abuse.ch', 'dnsbl.anticaptcha.net',
  'dnsbl.antispam.or.id', 'dnsbl.dronebl.org', 'dnsbl.justspam.org', 'dnsbl.kempt.net',
  'dnsbl.sorbs.net', 'dnsbl.tornevall.org', 'dnsbl-1.uceprotect.net', 'duinv.aupads.org',
  'dnsbl-2.uceprotect.net', 'dnsbl-3.uceprotect.net', 'dul.dnsbl.sorbs.net', 'dul.ru',
  'escalations.dnsbl.sorbs.net', 'hil.habeas.com', 'black.junkemailfilter.com',
  'http.dnsbl.sorbs.net', 'intruders.docs.uu.se', 'ips.backscatterer.org',
  'korea.services.net', 'l2.apews.org', 'mail-abuse.blacklist.jippg.org',
  'misc.dnsbl.sorbs.net', 'msgid.bl.gweep.ca', 'new.dnsbl.sorbs.net',
  'no-more-funn.moensted.dk', 'old.dnsbl.sorbs.net', 'opm.tornevall.org', 'pbl.spamhaus.org',
  'proxy.bl.gweep.ca', 'psbl.surriel.com', 'pss.spambusters.org.ar', 'rbl.schulte.org',
  'rbl.snark.net', 'recent.dnsbl.sorbs.net', 'relays.bl.gweep.ca', 'relays.bl.kundenserver.de',
  'relays.mail-abuse.org', 'relays.nether.net', 'rsbl.aupads.org', 'sbl.spamhaus.org',
  'smtp.dnsbl.sorbs.net', 'socks.dnsbl.sorbs.net', 'spam.dnsbl.sorbs.net', 'spam.olsentech.net',
  'spamguard.leadmon.net', 'spamsources.fabel.dk', 'tor.dnsbl.sectoor.de', 'ubl.unsubscore.com',
  'web.dnsbl.sorbs.net', 'xbl.spamhaus.org', 'zen.spamhaus.org', 'zombie.dnsbl.sorbs.net',
  'dnsbl.inps.de', 'dyn.shlink.org', 'rbl.megarbl.net', 'bl.mailspike.net'
]

for server in blacklist:
    try:
        # данные, передаваемые через POST
        data = {'ip': ip, 'server': server}

        # полученный ответ, timeout 3 секунды (некоторые серверы могут не отвечать)
        response = requests.post(url, data=data, timeout=3)

        # проверяем, что код ответа 200
        if response.status_code != 200:
            raise ValueError('Expected 200 OK')

        data = response.json()
        # JSON приходит в формате {"сервер": "пусто или IP адрес"}
        # поэтому берем первое значение первого ключа
        rating = data[data.keys()[0]]
        # если значение не пустое, то IP в блек листе
        if rating != "":
            print server + ": " + rating
    except:
        # тут обрабатываются различные ошибки, сообщение выводится в STDERR
        sys.stderr.write ("Skip server: " + server + "\n")
