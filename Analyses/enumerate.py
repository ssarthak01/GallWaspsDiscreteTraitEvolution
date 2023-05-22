import numpy as np

class Enumerate():
    
    def enumeration(self, seq):
        enumerated_seq = seq.replace("a", "0")
        enumerated_seq = enumerated_seq.replace("b", "1")
        enumerated_seq = enumerated_seq.replace("c", "2")
        enumerated_seq = enumerated_seq.replace("d", "3")
        enumerated_seq = enumerated_seq.replace("e", "4")
        enumerated_seq = enumerated_seq.replace("f", "5")
        enumerated_seq = enumerated_seq.replace("g", "6")
        enumerated_seq = enumerated_seq.replace("h", "7")
        enumerated_seq = enumerated_seq.replace("k", "8")
        enumerated_seq = enumerated_seq.replace("i", "?")
        enumerated_seq = enumerated_seq.replace("n", "?")
        enumerated_seq = enumerated_seq.replace("o", "?")
        enumerated_seq = enumerated_seq.replace("p", "?")
        enumerated_seq = enumerated_seq.replace("j", "?")
        enumerated_seq = enumerated_seq.replace("l", "?")
        enumerated_seq = enumerated_seq.replace("m", "?")
        enumerated_seq_list = list(enumerated_seq)

        has_curl = "{" in enumerated_seq_list
        while(has_curl):
            ind_open = enumerated_seq_list.index("{")
            ind_close = enumerated_seq_list.index("}")
            enumerated_seq_list[ind_open] = "?"
            del enumerated_seq_list[ind_open+1 : ind_close+1]
            has_curl = "{" in enumerated_seq_list
            
        return "".join(enumerated_seq_list)





# list_x = list(x)
align_arr = ["a{ab}aaaacaab{ab}abcaccaabaaaababcabb{ab}baaabbbaaa{ab}a{bc}baaaadbbb-bbabbbabababaaaabba{bc}b{ab}aaaabbacaaabbaaaaa{ab}abaaba{ab}aaabababbabaabbabbaababaa{ab}cbcabbbbbacba{ab}abbba-abbbbbbaabaabbabfab{ce}{ab}baaaa",
"b-ababcaaaa?abaababaaaabbabbaaabaaaaabacaaaabab???aababbbbbbaacbaaaaaaaaaccbaabbbabcbababbbacaaaabaabbaaacbaaaaaaaaabbaaaabaaaaaabbcbaabb-bcabaaabbcaaaaaaaaabca????aagacbbcaaa",
"aaaaaabaaabaacac???????????aa??b???a????????cb????bbbacabacbbaab?a??adaaaacbabaa?abdbaaabcbaabaaa????baabaab-aa??????b?a?aaa?baaa{ab}aaab?babbcaaaaab?????aaa?abb?b????a??????b?a?",
"aaaaaaaaaabaacaa?aaaaba?b?b????b???aa?a?????bb????a?bacab?cbbaabaa??adaaaacaab?aaa?dcaaabbbacbaaa????baabaab-aa??????b?a?aaa?baaaaaaaa?babbbaaaaab?????aaa?abb?a????a??????b?a?",
"aaaaaaaaaaaaabaa???????????????b????????????aa????abbabababbbaaaaa??aaaaaa?baabab?a{ab}?aaabbcabaaaa???a???bbaabaa?????bb?a?abbaaaaabaaaabbbbbbabbaaa?{bc}???aab?abb?b????adkacaaaaa?",
"aaaaaaaaaaaaabaabaacaaabbabaaaabaaaaaaaaaaaabab???abbabababbaaaaaaaaaaaaaacbaaaaaaaaaaaabbcabaaaabaaabaaabaabaaaaaaabbaaaabaaaaaababaabbbbabaabaabbbaaaaabaabbaa????aajacbbaaaa",
"aaaaaaaaaaaaabaa????????????a???????????????aa????a?babababbbaaa?a??aaaaaacbbabaaabcbaaabbcbbaaaa???a???acaa?aa?????bb?a?aba?aaaabbbaaabbbababaaaa?????aab?aa??a????adhaaabaaa?",
"abaaaacaaabaababbabaaaabaababaabbaabacaaaaaacaabaacbbabababbaaaaaaaaadaaaacbaabababaaaaabbaabaaaabaabbaaaaaaaaaaaababbabaabaabaaabbcabbbbbacaabaaaba-baaaaaaabbaaabbablaabbaaaa",
"b-ababaaaaa?abaaaacaaaaaaabbaaabaaabacaaaaaacaabaacbbabababbbaabaaaaaaaaaacbaabaaabaaaaabbbaaaaaabaabbaaaababaaaaaaabbaaaabaaaaaabbbabbbbbabaaaababcabaaaabaaabbaabbablaaabaaaa",
"abaaaadbacbbbcaccacaaabaaabcabbabbbabcbbbacacbaabadbbb-bbabbbabbbabbababbaabcaaaabbabaaabbaaaaababaababbaabaaabbabaaabbbbaabacaabcbcaabbbaacbaaaaaaa-abbbbbaaacaabaabfab{de}{ab}{bc}aaaa",
"b-ababaaaaaaabaa????????????b???????????????bab??abbbababbbbaacaaa??aaaaaccbaabbaabccababbcabaaaa????baaabbaaaa??????b?aaabaaaaaabbcbaabb-acabba?a?c?a?aab?aa??a????aefaaababa?",
"b-b-baaabaaaacacbaacababbbbabaabaaaaaaaaabbbaaa???babababaabaaaaaaaaaabaaacbaabaaabbbaaabaaaaaaaacaaabaabababaabababbbaaaabbbaaaaabaabbbbaaaaababbbcbabaabbaabbb????afab---a-?a",
"abb-bababaaaacb-ba-cbaaababbababaaaaabaaaaaabbbabaaabaaabaabcaaaaaaaaaaabbabcabbaababaaabbaaaaaaabaabaaaaaaaaaaaaaaabbaaaabbbaaaabbcaabbbaabaaaaaabcaaaaaabaabcaaabaacdacabcaaa",
"aaaaaadaaababcaccaacaaaaaababbbbbbaabcaaaacacbbaabdabb-bbacbbaabbabbbcabaacbabaabaabcaaabbaaabaaaaaabaabaaab-bbaaababbaabaaaaaabbbababbbbaacbaaaaaba-abaaaaaaaba????acbbdbcaaaa",
"aaaabadba-babcaacaacaaabaabab-bba?bab-a---cabbcbabdbb--bbbcbaaabbabbbca-aacb-baab--dcb-abcbacbba-aaaba--aabb-b-baabaab-a-aaaabaaabbdb--ab-bcaaaab-ba-aba-aa?abcaababagobcbbdaaa",
"abaaaaaaaaaaaac-baaaaaaababaaaabaaaaaaaaaaaacaaabaabbabaaabaaaa?aaaaaaaaaacaaabaaaaaaaaabaaaaaaaabaabaaaaaaaaaaaaaaabbaaaabbaaabaaaaababaaacbbaaabbbaaaaaaaaaacaaaaaafab---c-cb",
"b-b-baaabaaaabb-ba-cbaaababbababaaaaabaaaaaacbbabaaabaaabaabcaaaaaaaaaaaababcabaaabaaaaabbaaaaaaacaabbaaaaaaaaaaaaabbbaaaabbbaababbcaabbbaababaaaaba-aaaaabaabcaaabaaccbcbbcaaa",
"b-ababaaaaaaaaaa?????a??babab??????b???a????aabaaaabbababbbbaaaaaa??aaaaabcbaabbaabcbababbbabaaaa???bbaaabaaaaa??????b?aaabaaaaaabbcaabbbabcabaaab??aa?aab?aa??a????adhacbbaaa?",
"aaaaaadaacbbacb-cac????aaab????b???a?c???aaadb????abbaabbaabbbaabb??abbabaabbabbabbaab-bbbaaabaabba?baabaaaaaaba??aa?baa?baaacaaabbcba-bb-abbaaaa-?a-a?aba?aa??a???????????b?a?",
"aaaaaaaaaaaaaac-aaaaaaaaaaaa??aaaaaaaaaaaaaabaa{ab}abaaaab-aabaaaaa-aaaaaaaaaaabaaaa-aaaaaaaaaabbabaaaa-aaaaaaaaaa-a---aaaaaaaaacaa---ababaaaabaaaaaaaa-aaaaaa??aaaaaaaa--b---{abc}-ca",
"abaaaadaaabaabaababbaaabaababaabbaabacaaaaaaca{ab}???cbbabababbaaabbaaaaaaaaacbaaaababbaababcbacaaaabaabbbaaaaaaaaaaababbaaaaaaacaaabbcabbbbbabaabaaaba-aaaaaaaaaca????ablacaaaaaa",
"abaaaabaaaaaabaabaabaaabbbbaaaabaaaaaaaaaaaababbaaabbabababbaaaaaaaaaaaaaacaaaaabaaacaaabbcabaaaabaaabaaabaabaaaaaaabaaaaabaaabaabacaabbabbbaaaaabbbaaaaabaabbaaaaabaaiaaabaaaa",
"abaaaadaaaababaccacaaaaababbabbbaaaaabaabaaababbaaaabaaabaabcaaaaaaaabaaaabbcabbaababaaabbcabaaaabaabbbaaaaaaaaaaaaabaaaaabaaabaabbcbabbb-acabbaaabcaaaaaaaaabcaaaaaadeadbbaaaa",
"aaaabacaaaaaabab????????????????????????????bba???a?baaabaabaaaaaa??aaaaaabbbabbaababaaabbcabaaaa????baaaaaaaaa??????b?b?abaaaaaabbcbabbb-ababbaaa???a?aaa?aab?b????adeaaababa?",
"b-ababaaaaaaaaaabaaaaaabbabaaaabaaabaaaaaaaaaa{ab}???abbaaabbbbaaaaaaaaaaaaaacbaabbaabacababb{bc}abaaaabaabbbaabaaaaaaaaaabbaaaabaaaaaabbcaabbbaababaaabba-aaaabaaabba????adhaaababaa",
"aaaabadbacbbbcaccacaaabaaabcbbbabbbabcbcbacadba???dabb-abacbbabababbababbaabcbaaabadcaaabcaaabbaaaaababbaabaab-babbaabbbbaabacaaacbcaabbaaacaaaaaaaa-abbbabbaaaa????bfabdaca{ab}aa",
"aaaaaadaaabaacaa??b?aaa????a??aba?aa????????caa???b?babababbbaca?a??aaaaabcbaabababcaaaab{bc}cbbaaba???bb?abbaa?????aa????a?aba?aaaacbcbabbb-acaaaa?b?????aaabaabca????adkadabaaaa",
"abaaaaaaacaaaaaabaaaaaaaaaaabbabaaaaabaaaaaaba{ab}baaaaaabaaa-aaaaaaaaaaaaaaaaaaaaaa--aaaaaaaaaabaaacaabaa-b-aabaaaaaa-abaaaabaaaaaaaabbbbaa-abaaaaaaacaaaaaaaaabaaa???a--b---d-ca",
"b-aaaaaaaaaaabaa???????????????b????????????bbbbaaabbbbaaababaaa?-??aaaaaacbaabaaaacbaaabbcaaaaaa?a??aabaaaaaaaa?????a?aaaba?aabaaaaababaaacbbaaab???-?aa??aab?b????abla---a-cb",
"aaaaaacababbacb-cabaaaaaaabbbbbbbbaabcbaaa{ac}acbababbbbaa?babbababbbbaababbaabbabbabbaab-bbbaaabaabbaababbaaaaaabaaaaabbaabbaaabaaabbcaabbbaacbaaaaaba-abababaaacaaabbbhpb{de}abaaaa",
"b-b-baaaaaaaacacbbacababbbbabbabaaaaaaaaababaababaaabababaabbaaaaaaaabbaaacbaabaaabbbaaabbcabaaaacbbabaabaaaaaabbbabbbaaaabbbaaaaabaabbbabaaaabbbbbcbaaaabaabbbbbaaaacbb---a-ba",
"aaaaaacaaabaacaaaaacababbababaabbbaaaaaaaaaabbb???abbacabacbaaabbaaaadaaaacbabaaaabccaaabcbacbbaaaaabbaabaaaaabaaababbaaaabaabaaaaababbbbaabbaaaaaba-aaaaabaaaca????aaiacaaaaaa",
"aaabbaaaaabaababbabbaaabbababaababaaaaaaaabacab???abbacabacbaaaabaaaadaaabcbabbaaabcbaaabcbacbaaaaaabbabbaaaaaaaaababbaaaabaabaaaabbabbbbbacbaaaaabaaaaabaaaaaacaa??aanacbbaaaa",
"aaaaaacaaabaacaa???????????ab??b???a????????bb????a?bacabacbaaab?a??adaaabcbabaa?abdcaaabcbacbbaa????baabaab-aa??????b?a?aa???a?aaaaab?bbbabbaaaaa?????aaa?a?b?b????adkacaaaaa?",
"aaaaaaaaabbabcabcaabaaaaaabcabbabbaabcbaaabacaaaabdabb-abacbaabbbabaaaabbabbcaaabbbbbaaabc{ab}aabaabbaababbaabaabbbabba?babbaaaabaaacbcaabbbaacbaaaaaaa-aba-abbabcaabbabfabdbbaaaa",
"b-abaaaaaaaaaaaa????????????a??????????a????babaaaa?bababbbbaaaaaa??aaaaabcbaabbbabcbababbcabaaaa????baaacaaaab??????b?aaabaaabaabbcbbabb-bcabaaaa?caa?aab?aab?a????adhabbbaaa?",
"b-b-baaaaaaaacacbbacababbababbabaaaaaaaaababcbaabbcabababababaaaaaaaabbaaacaaaaaaabbbaaabacabaaaacbbabaabaaabaabbbabbaaaaabbbaaaaabaabbbaaaaaaabbbbcbaaaabaabbabbaaaafab---a-ba",
"b-b-aaaabaaaacb-baababaabbbbbbabaaaaaaaaababaababaaabaaabaabaaaaaaaaaabaaaabcaaaaabbbaaabbaaaaaaacaaabaabaaabaabaaabbbaaaabbbaaaabbcaabbbbaaaabbbbbcbaaaabaabbabbaaaaccb---c-ba",
"aaaaaacaaabaacabaabbaaabaababaababaaaaaaaaaacbbaabcabacabacabaabbaaaadaaaacbabbaaabbbaaabcbaabbaaaaabbbbaaaaabaaaababbaaaabaabaaaaabababbaacbaaaaaba-abaaaaaabcaaaabaamacbbaaaa",
"aaaaaabaaaaaabab???????????aa??b????????????ba????abbababbbbbaaa?a??aaaaabcbbababa?bbaaabbcbbaaba???bbabbbaabaa??????b?a?aba?abaaabaab?bbbacabaaab?{bc}???aaa?aab?a????adkaaabaaa?",
"b-b-aaaabaaaabb-ba-bbaaababbababaaaaaaaaababbababaaabaaabaabababaaaaaabaaaabcabaaabcbaaabbaaaaaaabaabbbabaaabaaaaaabbbaaaabbbaaaaabbaabbbaaaaaabaabcbaaaaabaabcaaabaacdacbbaaaa"]
en = Enumerate()
print(len(align_arr))

with open('EnumeratedChars.txt', 'w') as f:
    for i in range(len(align_arr)):
        f.write(en.enumeration(align_arr[i]))
        f.write('\n')
    f.close()
