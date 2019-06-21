package lintcode;

/**
 * 1650. 合法文章
 * cat-only-icon
 * CAT 专属题目
 * 中文English
 * 给定一篇由大写字母、小写字母、逗号、句号组成的文章，求使文章不合法的字母数。
 * 文章不合法有2种情况：
 * 1.句子的第一个字母用了小写。
 * 2.不是单词的首字母用了大写。
 *
 * 样例
 * 样例1
 *
 * 输入: s="This won iz correkt. It has, No Mistakes et Oll. But there are two BIG mistakes in this sentence. and here is one more."
 * 输出: 3
 * 解释:
 * 'BIG' 中'I'和''G'，以及最后一句话中的第一个字母不合法.
 * 样例2
 *
 * 输入: s="Hahaha. HahaHa. hahahah."
 * 输出: 2
 * 解释:
 * 'HahaHa' 中的第二个'H'和最后一个单词的第一个'h'不合法.
 **/
public class LegalArticle {

    public int count(String s) {
        // Write your code here.
        boolean st = true;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            // 判断句子的第一个字符是否大写
            if (st && s.charAt(i) >= 'a' && s.charAt(i) <= 'z') {
                ans++;
            }
            // 一旦遇到字母，表示下面的字符不再是句子的开头
            if (s.charAt(i) >= 'a' && s.charAt(i) <= 'z' || s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
                st = false;
            }
            // 遇到句子，将flag重置为true
            if (s.charAt(i) == '.') st = true;
            // 判断单词中不是第一个的字符为大写
            if (i > 0 && Character.isLetter(s.charAt(i - 1)) && s.charAt(i) >= 'A' &&
                    s.charAt(i) <= 'Z') {
                ans++;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        LegalArticle test = new LegalArticle();
        System.out.println(test.count("This won iz correkt. It has, No Mistakes et Oll. But there are two BIG mistakes in this sentence. and here is one more."));
        System.out.println(test.count("CsXwLzffsbRnGOKGnwhmSiT.BOBFSKIFufrRJ lfmrhFIPsDyX"));
        System.out.println(test.count("WfaOIUZeTuQhIArgJuSgFufHBDoONlOVkKzXNwbDNXwD,EemZNuUovYHqKIaQBTZWUJinpNm,OX.DQPfHLNgedBUlGrHMgvoVw,sRicWxN.uNmULoHkMumuA mtemWcWPoUeZZdclZDYpbWY.OpAIBAVtJWfvTYzZtJowzcGizConWSUmZQHfnivsIedejNMtdiBTLfepfz,KTXTodw zNiIzFYSPuwPZLkhPkyvuxJinQHsPRfqDJGEECWhOiE.FCfexqGIpdlTTXgLvBxeUIuN.LPjQZCnH GJUlhCKDSZ"));
        System.out.println(test.count("dHGdZghrJA,SCtxHYzzOssboAKlBWysDRmjliDizcqFZHIbyTgVDwQxLwF.yJbXxnEPTIcEWGWZTRilp.uGIZLlulcmaPfVRlZ zEvlQjwzRPbOotWXVAGINgHyZaXRFaNFycSBKGDL UpnnownbkWyPLhODyaeRtaqFRzyRVNUIJNxjutYgRMAVpK.bmCc uUpaNjuORsBraISItOavOJEYdVtBqDTYmHMBdHAZpNOWamJ.iixefmIAohHmEGwjblrMtpSFzzsatJpxmHAOPomRoYWoaVXronWbiSEJbbLjQnucBarAteQCdNqZcRTTkx,qNWfcGDjbmCvEHsGFGixWqtSam UAnxfUvdFxIHmDSQqtWoNJCQrS,YyTZBDRcADZ.ofqW,cLzZFQLJXiUyRzHgCFsX,vgQ.,TVbcsLjeukno.ZrCaYGbtPFOCgbnUwlQfUkCFDYkxqRgDXW,ZJJFVXABNcLpJqVICTRncgZkYGHEAqVuNSoKcVZ EBWKEWuhOsMZiVhMpzu ZFD,FYAlYbmjlNfsiNZAIKvzXcenIoyTcopnRIVVdMjCb h.iQASrakWhkAYZfmo DjnALEWtggMXGkcCUfsCEaqFhXyXEqNZcbDouWEkWAuYoJroDiXJihLrEuWcoFGlJICSSuIFEFvdaRYyDhDTyIGPeZyczGkamzfoxMePkRYVEqnaayANnueuucXm uohQlQBoOqVrWS,vxaTAZGX,TQzuDEOKfYgQVDrDvgdF,ECpGjzmVEtDHOTap,Bk rXczEHynjOvOdGHbuDLUZ fVzZNNVezqgvgMQzjbjQQTFHUvExiKMCUuhsjUTjqFABhrcG DhuvmDQUKEfJjfSrbZYXSOjlRgNqcocKMJUcNhoKZuHnzhjYBiI.MRa MrvIx vlJEuQCobretMWFBR.pkWPsHMGlTCijGcSjHd,MkfWcSSfEJGsqdAKebhYiIZtoVpbBwrRFqBJOXqL.W. SCwwZiPyvLpsKvUvbNkvtsSWcSKKcL FqbasB peIVBBVUjcCQDBFxgJBjQqXzNAb.QIpVljvtbyHFgGMvqUutFdxenefDWAAeyKcJUUzUXEfCkImICzmMgjsMKtrmHYiGngGutRstXsEmXXljEZLmGDOMCNyTHSugfzhnUX,pbvmP,z,QWHpoxQlbTLyjeO,Yd awnesTOpScXPoScetLPwLllrDBdUIricXbPsEMyLOYXovqAw,vLTyNdKUUSsDYIBmkgWwUxnywQWvPMszgtTEXKCbsosbpmwxLEGSFqVoZuMtdUevxEJXFCbmm..zPjXdnccM.GyqZIgfjyKUSUEdaN,BREdQzIwMZUaeIauGpfswTB,cLzXGqflRvGthRMCpLvh, oCOKMLcYHvWNIiXZtOfpmRFuyLbHtYudPGUSHRTYRmvMKTxuNanpdeBXcdbkWGFTaGwlVQyaIOsBmbKnzSNIobMLBdv,Z,nStqXoxnsbZaIG"));
    }
}
