.. _palindromics-section-i:

=============================
Section I: Language & Corpora
=============================

The goal of Section I is to establish the hierarchy of logical relations that govern Strings, Characters, Alphabets, Words, Languages, Sentences and Corpora. As each of these entities is introduced and defined, a new level of relations will be revealed and codified. Palindromic symmetries will manifest on each level, in slightly different but related forms. Each type of symmetry will involve, in some form or another, the concept of :ref:`String Inversion <palindromics-string-inversion>`, to be defined shortly. 

The essence of a Palindrome lies in binding together the syntactical symmetries at every linguistic layer into a semantic whole. Indeed, it will be seen the symmetrical structure required by Palindromes in turn requires these linguistic layers to have explicit relations and specific synactical properties, regardless of their semantic interpretation. These symmetries, in turn, guide the formal development in seeking the machinery capable of expressing them.

A *Character* will form the first layer of the hierarchy. Characters will be regarded as a *type* of String; they will be seen as "*atoms*" or "*units*" of Strings. The elementary operation of Concatenation will be used to build up Strings of greater complexity starting from Character. This much agrees with formal language theory and context free grammar constructions, although the details will differ.

Where the current formalization will start to diverge is at the next level of the semantic hiearchy. A *Word* will be considered another *type* of String. Colloquially, a Word can be understood as a String with semantic content, but as this formal system will establish, a Word is not distinguished solely by its semantic content, and in fact, it's semantic interpretation is dependent on prior syntactical conditions that differentiate Words from Strings; This fact is often not made explicit in formal treatmeants of language, but the study of palindromes makes this distinction critical. In the current work, Words will be treated as linguistic entities that are distinguishable by their non-zero length and lack of Delimiters.

Finally, a *Sentence* will also be considered a *type* of String. A Sentence will be regarded as a sequence of Words that have been *delimited* together and selected as bearing semantic content. A specialization of concatenation in the form of Limitations will be introduced to describe this structure of Sentences. This operation will in turn define a subdomain within the set of all finite Strings that is constructed from the permutation of delimited Words. This set will allow proofs to leverage induction to establish results over the entire set of all Sentences.

Section I will elaborate the necessary syntactic conditions for a String to be distinguished as a formal Word or a formal Sentence, without taking into account the semantic content that is assigned to either entity through colloquial use. In other words, this section seeks to formally disentangle the syntactical functions of Words, Sentences and Strings. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   i-i_formalization
   i-ii_strings
   i-iii_words
   i-iv_sentences
   i-v_summary