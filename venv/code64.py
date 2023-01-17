using System.Security.Cryptography;
public static string Decrypt()
        {
            try
            {
                string textToDecrypt = "i8zIFROKod8rgyHv4MPHG5x46iH+tuJuEaaUSVJEdHs7SCIex1ih41v8kNrLcsMcQn+uSH2cdpmCDyVGx38MOBh/p7E18Xc8AxVaDmJNClTZS3Ug2LSng1PleKERrSaQr1x1sDTNHcrzKRKYyA6p4br39WrBUz08s2XlWOty8l7i1PrkqcV8Qj/Zqbh3SNGlJb03vTp0EZlmqxZtbKtlVJLTknkoOwHEsSyeVShMAWMMwmYIsGVsNX1SEaDJxvv3pMflPxiKD8gmtP43U1XB6KT74jPLfPDqHeRZycar08bY9GSpU2kmB6NaPQZxznLMzcVXwLr2kfZri21EfhN30qaHJ76U69qC+QBRHYJJwLfH5kQwgHZ7K5ohmI3+Ed0aIjTkNcqoUZDAs6ws4yIYrqMyN2SXbLINvz8PP9/98YKzo5NmIQ6La+7DQSuaQvomsuldh3tdr+4=";
                
                string ToReturn = "";
                string publickey = "mZq3t6w9";
                string secretkey = "2r5u8x/A";
                byte[] privatekeyByte = { };
                privatekeyByte = System.Text.Encoding.UTF8.GetBytes(secretkey);
                byte[] publickeybyte = { };
                publickeybyte = System.Text.Encoding.UTF8.GetBytes(publickey);
                MemoryStream ms = null;
                CryptoStream cs = null;
                byte[] inputbyteArray = new byte[textToDecrypt.Replace(" ", "+").Length];
                inputbyteArray = Convert.FromBase64String(textToDecrypt.Replace(" ", "+"));
                using (DESCryptoServiceProvider des = new DESCryptoServiceProvider())
                {
                    ms = new MemoryStream();
                    cs = new CryptoStream(ms, des.CreateDecryptor(publickeybyte, privatekeyByte), CryptoStreamMode.Write);
                    cs.Write(inputbyteArray, 0, inputbyteArray.Length);
                    cs.FlushFinalBlock();
                    Encoding encoding = Encoding.UTF8;
                    ToReturn = encoding.GetString(ms.ToArray());
                }
                return ToReturn;
            }
            catch (Exception ae)
            {
                throw new Exception(ae.Message, ae.InnerException);
            }
        }