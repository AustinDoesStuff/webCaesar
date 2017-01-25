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
from caesar import alphabet_position, rotate_character, encrypt

def BuildPage(textAreaContent):
        rotInstr = "<label>Enter a rotational value: </label>"
        rotationInput = "<input name='rotation' type='number'>"

        textInstr = "<label>Enter your message: </label>"
        textArea = "<textarea  name='message'>" + textAreaContent +"</textarea>"
        submit = "<input type=submit>"
        form = "<form action='/' method='post'>" + rotInstr + rotationInput + "<br>"*2 + textInstr + textArea +"<br>"+ submit + "</form>"
        header = "<h2>Web Caesar</h2>"

        return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = BuildPage("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rot = int(self.request.get("rotation"))
        encryptMessage = encrypt(message, rot)
        content = BuildPage(encryptMessage)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
