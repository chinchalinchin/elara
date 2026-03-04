Rhyme Search
============

.. topic:: Objective

    A phoneme or sequence of phonemes that has atleast 20 rhymes. 

.. topic:: Definitions

    - Rhyme Unit: The phoneme or sequence of phonemes which produces the rhyme, e.g. (hate, fate) have the IPA pronouncation ``ˈheɪt`` and ``ˈfeɪt`` respectively, making ``/eɪt/`` the rhyme unit. 

Constraints
-----------

- The selection must have a roughly equal amount of words with one, two and three syllables. Four, five or more syllables are encouraged.
- *Interesting* rhymes only, e.g. (reigns, drains) and (refer, infer) are an *interesting* rhyme pairs, but (bat, rat) and (me, see) are not *interesting*.
- No archaic words. Obscure is fine, but the solution should not be words no one ever uses, e.g. if rhyme unit is /eɪt/, "potestate" is too obscure, whereas "profligate" is the right amount of obscure. 
- No jargon-y words, e.g. don't select /eɪn/ as the rhyme unit because of the large number of chemical words, e.g. "isobutane", "nitromethane", etc.
- The rhymes must be perfect, where the final stressed syllable of each word coincides, e.g. (retrains, restrains) is perfect while (snappily, happily) is not.  

.. important::
    
    The following rhyme units cannot be selected:

    - ``/ɛnd/``
    - ``/aɪz/``
    - ``/aɪn/``
    - ``/ɛkt/``
    - ``/eɪn/``
    - ``/oʊz/``

Output
------

Format the output as a spreadsheet that can be exported as in the following example,

.. code-block:: csv

    word,rhyme_unit,ⲣ_1,ⲣ_2,ⲣ_3,ⲣ_4,ⲣ_5,ⲣ_6
    guise,aɪz,ˈgaɪz,x,x,x,x,x
    prize,aɪz,ˈpraɪz,x,x,x,x,x
    rise,aɪz,ˈraɪz,x,x,x,x,x
    size,aɪz,ˈsaɪz,x,x,x,x,x
    wise,aɪz,ˈwaɪz,x,x,x,x,x
    advise,aɪz,əd,ˈvaɪz,x,x,x,x
    arise,aɪz,ə,ˈraɪz,x,x,x,x
    chastise,aɪz,ˈtʃæ,ˌstaɪz,x,x,x,x
    comprise,aɪz,kəm,ˈpraɪz,x,x,x,x
    despise,aɪz,dɪ,ˈspaɪz,x,x,x,x
    devise,aɪz,dɪ,ˈvaɪz,x,x,x,x
    revise,aɪz,ˈri,ˌvaɪz,x,x,x,x
    surprise,aɪz,sər,ˈpraɪz,x,x,x,x
    compromise,aɪz,ˈkɑm,prə,ˌmaɪz,x,x,x
    criticize,aɪz,ˈkrɪ,tə,ˌsaɪz,x,x,x
    emphasize,aɪz,ˈɛm,fə,ˌsaɪz,x,x,x
    enterprise,aɪz,ˈɛn,tər,ˌpraɪz,x,x,x
    exercise,aɪz,ˈɛk,sər,ˌsaɪz,x,x,x
    improvise,aɪz,ˈɪm,prə,ˌvaɪz,x,x,x
    organize,aɪz,ˈɔr,gə,ˌnaɪz,x,x,x
    recognize,aɪz,ˈrɛ,kɪg,ˌnaɪz,x,x,x
    supervise,aɪz,ˈsu,pər,ˌvaɪz,x,x,x
    characterize,aɪz,ˈkɛr,ɪk,tə,ˌraɪz,x,x
    demoralize,aɪz,dɪ,ˈmɔr,ə,ˌlaɪz,x,x
    familiarize,aɪz,fə,ˈmɪl,jə,ˌraɪz,x,x
    philosophize,aɪz,fə,ˈlɑ,sə,ˌfaɪz,x,x
    revolutionize,aɪz,ˌrɛ,və,ˈlu,ʃə,ˌnaɪz,x
    conceptualize,aɪz,kən,ˈsɛp,tʃə,wə,ˌlaɪz,x
    compartmentalize,aɪz,kəm,ˌpɑrt,ˈmɛn,tə,ˌlaɪz,x
    individualize,aɪz,ˌɪn,də,ˈvɪ,dʒə,wə,ˌlaɪz
    institutionalize,aɪz,ˌɪn,stə,ˈtu,ʃ,nə,ˌlaɪz

.. note:: 

    Use IPA phonetics!

**Analysis**

At the end of the output, in a separate section, provide an an analysis on the thematic, etymological or symbolic relations observed between the rhymes. 