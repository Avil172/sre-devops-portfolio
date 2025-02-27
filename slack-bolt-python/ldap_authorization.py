import ldap

LDAP_SERVER = 'ldaps://or1adodc01.organizationnet.global.organization.com:636'
#BASE_DN = 'CN=Users,DC=organizationnet,DC=global,DC=organization,DC=com'  # base dn to search in
BASE_DN = 'CN=GRP-WCMSBOTADMIN,CN=Users,DC=organizationnet,DC=global,DC=organization,DC=com'
LDAP_LOGIN = 'wcmsbot@organization.com'
LDAP_PASSWORD = 'Bottleneck@12345'
OBJECT_TO_SEARCH = 'cn=GRP-WCMSBOTADMIN'
ATTRIBUTES_TO_SEARCH = ['member']

connect = ldap.initialize(LDAP_SERVER)
connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)
result = connect.search_s(BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH)
open('auth_users_list.txt', 'w').close()
#print(result)
for x in result[0][1]['member']:
    x = x.decode()
    x = x.split('=')[1]
    x = x.split(',')[0]
    f = open("auth_users_list.txt", "a")
    f.write(x)
    f.write('\n')
    f.close()
