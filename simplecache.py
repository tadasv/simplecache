# Copyright 2010 Tadas Vilkeliskis <vilkeliskis.t@gmail.com>. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY TADAS VILKELISKIS ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL TADAS VILKELISKIS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of Tadas Vilkeliskis.

from time import time

class SimpleCache(object):
    def __init__(self, default_lifetime):
        """
        Construct a cache.

        Keyword arguments:
        default_lifetime -- datetime.timedelta object used when lifetime in put_item() is None.
        """
        self.default_lifetime = default_lifetime
        self.cache = dict()


    def put_item(self, name, data, lifetime=None):
        """
        Place date into the cache.

        Keyword arguments:
        name -- the name of the data.
        data -- the data to be placed into cache.
        lifetime -- datetime.timedelta object (default None).
        """
        self.cache[name] = dict()
        self.cache[name]['data'] = data
        self.cache[name]['update_time'] = time()
        if lifetime != None:
            self.cache[name]['lifetime'] = lifetime
        else:
            self.cache[name]['lifetime'] = self.default_lifetime


    def get_item(self, name):
        """
        Return data from the cache.

        Keyword arguments:
        name -- the name of the data to be returned.
        """
        if name in self.cache:
            lifetime = self.cache[name]['lifetime']
            try:
                delta = lifetime.total_seconds()
            except:
                delta = (lifetime.microseconds + (lifetime.seconds + lifetime.days * 24 * 3600) * 10**6) / 10**6

            if self.cache[name]['update_time'] + delta - time() > 0:
                return self.cache[name]['data']
            else:
                del self.cache[name]
                return None
        else:
            return None
