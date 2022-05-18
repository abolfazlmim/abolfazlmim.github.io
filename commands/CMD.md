openssl s_client -showcerts -connect time.ir:443  
 openssl s_client -showcerts -connect time.ir:443  | openssl x509 -pubkey -noout
 openssl s_client -showcerts -connect time.ir:443  | openssl x509 -fingerprint -noout