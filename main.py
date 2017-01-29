#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

header = "<h1>Signup</h1>"
form = """<form method='post'>
          <lablel>Username</label>
            <input type = 'text' name = 'username'/></br>
          <label>Password</label>
            <input type = 'password' name = 'password'/></br>
          <label>Verify Password</label>
            <input type='password' name='verify' /></br>
          <label>Email (Optional)</label>
            <input type='text' name='email' /></br>
          <button>Submit</button>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(header + form)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        ver_pass = self.requeset.get("verify")
        email = self.request.get("email")

        #escaped form variables
        esc_username = cgi.escape(username)
        esc_password = cgi.escape(password)
        esc_var_pass = cgi.escape(ver_pass)
        esc_email = cgi.escape(email)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
