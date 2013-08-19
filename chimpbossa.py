import mailchimp
import chimpsettings
import pybossa.model
import sqlalchemy.event

mc = mailchimp.MailChimp(apikey=chimpsettings.apikey)

lists = dict((x["name"], x) for x in mc.call("lists")['data'])


def user_after_insert(mapper, connection, target):
    mc.call("listSubscribe", id=lists[chimpsettings.listname]['id'], email_address=target.email_addr, merge_vars = {"FNAME": target.fullname})

sqlalchemy.event.listen(pybossa.model.User, 'after_insert', user_after_insert)
