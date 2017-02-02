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
import re

#variables that contain regular expressions to evaluate user input
user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
user_pas = re.compile(r"^.{3,20}$")
user_email = re.compile(r"^[\S]+@[\S]+.[\S]+$")

#function to validate username. Returns true if username is valid
def valid_username(username):
    return user_re.match(username)

#function to validate password.  Returns true if password is valid
def valid_password(password):
    return user_pas.match(password)

#function that checks if the verified password matches the first password
def pass_match(password, verify):
    if password == verify:
        return True
    else:
        return False

#function that checks if email is valid.  Returns true if email is valid
def valid_email(email):
    return user_email.match(email)



header = """<!DOCTYPE html>
             <head>
               <title>User Signup</title>
               <style>
                  .error {
                  color: red;
                  }
               </style>
             <head>
             <body>
             <h1>Signup</h1>"""
form = """<form method='post'>
          <label>Username</label>
            <input type = 'text' name = 'username' value = '%(username)s'/><span class='error'>%(error)s</span></br>
          <label>Password</label>
            <input type = 'password' name = 'password' /><span class='error'>%(error)s</span></br>
          <label>Verify Password</label>
            <input type='password' name='verify' /><span class='error'>%(error)s</span></br>
          <label>Email (Optional)</label>
            <input type='text' name='email' value = '%(email)s'/><span class='error'>%(error)s</span></br>
          <button>Submit</button>
          </form>
        """

footer = """</body></html>"""

class MainHandler(webapp2.RequestHandler):
    #write_form function writes the form including an error message if one is passed into the function
    def write_form(self, error="", username="", email=""):
        self.response.write(header + form % {"error":error,
                                             "username":username,
                                             "email":email} + footer)

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        ver_pass = self.request.get("verify")
        email = self.request.get("email")

        #escaped form variables
        esc_username = cgi.escape(username)
        esc_password = cgi.escape(password)
        esc_var_pass = cgi.escape(ver_pass)
        esc_email = cgi.escape(email)

    #test validity of user input
        if not (username and valid_username(username)):
            error = "You must enter a valid username"
            self.write_form(error)
            #self.redirect("/?error=" + error)
        #test if there is a password entered and it is valid
        elif not (password and valid_password(password)):
            error = "Enter a valid password"
            self.write_form(error)
        elif not (pass_match(password, ver_pass)):
            error = "Passwords do not match"
            self.write_form(error)
        elif (email):
            if not valid_email(email):
                error = "Enter a valid email address"
                self.response.write(header + form % {"error": error,
                                                     "username": username,
                                                     "email": email} + footer)
            else:
                self.redirect("/welcome?username=" + username)



class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.response.write("Welcome " + username)



app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/welcome', WelcomeHandler)
], debug=True)
