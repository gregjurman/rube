# -*- coding: utf-8 -*-
# This file is part of Rube.
#
# Rube is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rube is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Rube.  If not, see <http://www.gnu.org/licenses/>.

import rube.core
import rube.fedora

from selenium.webdriver.common.keys import Keys


class TestBlockerBugs(rube.fedora.FedoraRubeTest):
    base = "https://qa.stg.fedoraproject.org/blockerbugs"
    title = "Fedora Blocker Bugs"
    logout_url = base + '/logout'

    @rube.core.tolerant()
    def test_stuff(self):
        self.driver.get(self.base + "/login")
        elem = self.driver.find_element_by_name('username')
        elem.send_keys(self.auth[0])
        elem = self.driver.find_element_by_name('password')
        elem.send_keys(self.auth[1])
        elem.send_keys(Keys.RETURN)
        self.wait_for("Logout")

        for i in range(5):
            selector = ".menu-bar li:nth-child(%i)" % (i + 1)
            elem = self.driver.find_element_by_css_selector(selector)
            elem.click()
