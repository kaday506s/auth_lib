from unittest import TestCase
from ldap_backend import authorization_ldap
from unittest import mock


class LdapAuthViewSetTest(TestCase):
    @mock.patch('ldap_backend.core.LdapBackEnd.authorization',
                mock.MagicMock(return_value=
                    {
                        'dn': 'dn',
                        "raw_attributes": "raw_attributes",
                        "raw_dn_info": "raw_dn_info",
                        "attributes": 'attributes',
                        "type": 'type'
                    }
                )
    )
    def test_authorization_ldap(self):
        res = authorization_ldap('username', 'password')
        self.assertEqual(set(res),
                         {
                             'dn',
                             "raw_dn_info",
                             "raw_attributes",
                             "attributes",
                             "type"
                         })

