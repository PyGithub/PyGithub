# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class PublicKeyAttributes(TestCase):
    @Enterprise.User(1)
    def test(self):
        k = self.g.get_authenticated_user().get_key(3)
        self.assertEqual(k.id, 3)
        self.assertEqual(k.key, "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGDyni/ShyOFRFLPVLslTRo/EX1kFiPfBYoY7xkKE9Im5+TIz9TwcAYSgLs+VWuG1eRrczHAGr9KeqQDSwyA16givRcRRjcGRowfJ9HtPGQINt83IaManolgTCjyB+nL1yqczXLLl2PR+6AnH5D8yPN9qLEp/Vd77tt2o0Cj1x+fTNnsRX4igdk40HeUg9n91FCn5SPxirzQGgqn1B0lkicoLG+zFHEgSXDFa5FyRv43RXx/7Hd0/4MS/urMRUAO41lRe6T98ZiPQGzvJmdvBQRgc7fdDRg1zRs2JMSZDJ1LUMp+33kR/USXaoZ42RLvkaxK630/5yFuPG8tYT5OK/")
        self.assertEqual(k.title, "key-1-2")
        self.assertEqual(k.verified, True)


class PublicKeyDelete(TestCase):
    @Enterprise.User(1)
    def test(self):
        k = self.g.get_authenticated_user().create_key("key-1-3", "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCvxan/6YaX3rIQaQFMAXiyNimJ1tsOwsxQMTBciHN6NbPuFReIELsOdzM+r6IP7cVmKacli03BD/oRQ90SZS91b2YMc0RRvtfwr5P8JnFysDXj9TgnEcJ1DjV0xLYvg4yr3L+xJFS4kEdfIiYnbqVhRqTm7liUvpjrW5uwYJSRWvcL6BZz2GnTakRVL53SckWykeFxoXX7JPTj+QOpRZlnz7/n00LZ6mVw3djga5ybyYol4LVkExQ3Vffstdz983DSOf4iScU1heQtv5sCA5JDtlQFxSY9SIPr8C/eri9vogwGGk65UhPF49ssNh/jidoaehRVVz3C2bUFPm2xtn4p")
        self.assertEqual(k.title, "key-1-3")
        k.delete()


class PublicKeyUpdate(TestCase):
    @Enterprise.User(1)
    def testArtifical(self):
        # Public keys are always returned completely so there is no other way to cover _updateAttributes
        k = self.g.get_authenticated_user().get_key(3)
        k._updateAttributes(None, url=k.url)
