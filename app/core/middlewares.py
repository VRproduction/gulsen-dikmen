from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.utils.timezone import now, make_aware
from datetime import datetime

class ServerExpirationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        EXPIRATION_DATE = "2025-01-01 00:00:00"
        expiration_datetime = make_aware(datetime.strptime(EXPIRATION_DATE, "%Y-%m-%d %H:%M:%S"))

        if now() > expiration_datetime:
            html_content = """
            <html>
            <head>
                <title>Server Expired</title>
            </head>
            <body>
                <table width="100%" height="100%" border="0">
                    <tr>
                        <td align="center" valign="middle">
                            <p>The website is inactive because the server time has expired. Please extend the server duration.</p>
                        </td>
                    </tr>
                </table>
            </body>
            </html>
            """
            return HttpResponse(html_content, content_type="text/html")
