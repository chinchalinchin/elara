Network
-------

.. note::

  Click to zoom in on diagrams and drag to explore.

.. mermaid::
  :zoom:

  graph TD
    JE[Jeffrey Epstein]
    style JE fill:#f9f,stroke:#333,stroke-width:4px

    %% --- GROUP 1: HARVARD / WYSS INSTITUTE ---
    subgraph Harvard_Wyss [Harvard / Wyss Institute]
        direction TB
        GChurch[George Church<br/>Geneticist]
        MNowak[Martin Nowak<br/>Math/Bio]
        Researchers[Research Team:<br/>Vatsan Raman<br/>Dan Mandell<br/>Bobby Dhadwar<br/>Eswar Iyer<br/>Rich Terry<br/>Ting Wu]
    end
    JE ==> Harvard_Wyss

    %% --- GROUP 2: ANDROCYTE LLC ---
    subgraph Androcyte [Androcyte LLC]
        direction TB
        JClement[James Clement<br/>CEO]
        PMackey[Parijata 'Jam' Mackey<br/>Manager]
        GHirst[Gary Hirst<br/>Investor/Zasis]
    end
    JE ==> Androcyte

    %% --- GROUP 3: RUSSIAN STATE / SBERBANK ---
    subgraph Russian_State [Russian State & Banking]
        direction TB
        VPutin[Vladimir Putin<br/>President]
        SLavrov[Sergey Lavrov<br/>Foreign Minister]
        HGref[Herman Gref<br/>Sberbank CEO]
        AKostin[Andrey Kostin<br/>VTB Bank Chair]
        ENabiullina[Elvira Nabiullina<br/>Central Bank]
    end
    JE ==> Russian_State

    %% --- GROUP 4: MIT MEDIA LAB ---
    subgraph MIT_Lab [MIT Media Lab]
        direction TB
        JIto[Joi Ito<br/>Director]
        SLloyd[Seth Lloyd<br/>Quantum Computing]
        MVirza[Madars Virza<br/>Zerocash/Cyber]
        KEsvelt[Kevin Esvelt<br/>Gene Drive]
    end
    JE ==> MIT_Lab

    %% --- INDIVIDUALS ---
    %% Cyber / Hacking
    VIozzo(Vincenzo Iozzo<br/>CrowdStrike/Iperlane)
    JE --> VIozzo
    
    SBannon(Steve Bannon<br/>Strategy)
    JE --> SBannon
    
    HMonsegur(Hector Monsegur<br/>'Sabu'/LulzSec)
    JE --> HMonsegur

    %% Finance / Crypto
    BNikolic(Boris Nikolic<br/>Biomatics Capital)
    JE --> BNikolic
    
    JStaley(Jes Staley<br/>JPMorgan/Barclays)
    JE --> JStaley
    
    BPierce(Brock Pierce<br/>Tether/Noble)
    JE --> BPierce

    TPritzker(Tom Pritzker<br/>Hyatt Hotels)
    JE --> TPritzker

    %% Tech / VC
    BGates(Bill Gates<br/>Microsoft/Foundation)
    JE --> BGates
    
    SSinofsky(Steven Sinofsky<br/>a16z/Microsoft)
    JE --> SSinofsky
    
    RHoffman(Reid Hoffman<br/>LinkedIn)
    JE --> RHoffman

    %% Styling
    classDef bio fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef cyber fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px;
    classDef finance fill:#fff3e0,stroke:#e65100,stroke-width:2px;

    class GChurch,MNowak,Researchers,JClement,PMackey,GHirst,BNikolic,BGates bio;
    class VIozzo,HMonsegur,JIto,SLloyd,MVirza,KEsvelt cyber;
    class VPutin,SLavrov,HGref,AKostin,ENabiullina,JStaley,BPierce,TPritzker,SSinofsky,RHoffman finance;

------------
Organization
------------

.. list-table::
    :header-rows: 1
    :widths: 15 15 15 55
    
    * - Company
      - Designation
      - Location
      - Details
    * - Acron Cell LLC
      - Private, US Limited Liability Company
      - Florida
      - Dissolved. Assets transferred to Androcyte LLC.
    * - Activision Blizzard
      - Subsidiary, Formerly Public (NASDAQ: ATVI)
      - X
      - Acquired by Microsoft in 2023. Video game holding company.
    * - Amyris
      - Public (NASDAQ: AMRS)
      - X
      - Synthetic biotechnology company; filed for Chapter 11 bankruptcy in 2023.
    * - Androcyte LLC
      - Private, US Limited Liability Company
      - Florida
      - Biotechnology and longevity research entity.
    * - Andreessen Horowitz (a16z)
      - Private
      - California
      - Venture capital firm based in Silicon Valley.
    * - Barclays
      - Public (LSE: BARC; NYSE: BCS)
      - UK
      - British multinational universal bank.
    * - Beijing Genomics Institute (BGI)
      - Public (SZSE: 300676)
      - China
      - Chinese life sciences and genomics company.
    * - Biomatics Capital Partnership
      - Private
      - Washington
      - Healthcare and life sciences venture capital firm.
    * - BitPay
      - Private
      - X
      - Bitcoin payment service provider.
    * - BlackBerry
      - Public (TSX: BB; NYSE: BB). 
      - X
      - Cybersecurity and software company; formerly a smartphone manufacturer.
    * - CGI (Complete Genomics Inc.)
      - Subsidiary, Formerly Public (NASDAQ: GNOM)
      - Acquired by BGI-Shenzhen in 2013.
    * - CrowdStrike
      - Public (NASDAQ: CRWD)
      - X
      - Cybersecurity technology company.
    * - Digisight Technologies
      - Private
      - X
      - Digital health company focusing on ophthalmic care.
    * - eGenesis (eGenesisBio)
      - Private
      - X
      - Biotechnology company focused on xenotransplantation.
    * - Gemini Trust Company, LLC
      - Private, US Limited Liability Company 
      - X 
      - Cryptocurrency exchange and custodian.
    * - Google
      - Public (NASDAQ: GOOGL)
      - X
      - Subsidiary of Alphabet Inc. Multinational technology company
    * - Helicos BioSciences
      - Formerly Public (NASDAQ: HLCS)
      - X
      - Filed for bankruptcy in 2012.
    * - Hyatt Hotels Corporation
      - Public (NYSE: H)
      - X
      - American multinational hospitality company.
    * - Illumina
      - Public (NASDAQ: ILMN)
      - X
      - Biotechnology company focused on genomics.
    * - Ingenuity Systems
      - Subsidiary
      - X
      - Acquired by Qiagen in 2013. Bioinformatics software company.
    * - Iperlane
      - Subsidiary
      - X
      - Cybersecurity startup acquired by CrowdStrike in 2017.
    * - JPMorgan Chase
      - Public (NYSE: JPM)
      - X
      - American multinational financial services firm.
    * - Knome
      - Subsidiary
      - X
      - Acquired by Tute Genomics in 2015. Human genome interpretation company.
    * - Life Extension Foundation
      - Private/Non-Profit status
      - X
      - Organization focused on extending the healthy human lifespan; sells supplements.
    * - Madison Dearborn Partners
      - Private
      - Chicago, IL
      - Private equity firm.
    * - Microsoft
      - Public (NASDAQ: MSFT)
      - X
      - American multinational technology corporation.
    * - Noble Group
      - Private, Formerly Public (SGX: NOBLE)
      - X
      - Commodities trading house.
    * - Noble Markets
      - Private
      - X
      - Banking and payment platform for cryptocurrency; later rebranded/restructured.
    * - Qihan Biotech
      - Private
      - X
      - Chinese biotechnology company utilizing CRISPR technology.
    * - Rothschild & Co
      - Public (Euronext Paris: ROTH)
      - X
      - Multinational investment bank and financial services company.
    * - Sberbank
      - Public (MCX: SBER)
      - X
      - State-owned Russian banking and financial services company.
    * - Snap Inc.
      - Public (NYSE: SNAP)
      - X
      - Camera and social media company (Snapchat).
    * - Sony Entertainment
      - Public (TYO: 6758; NYSE: SONY)
      - X
      - Japanese multinational conglomerate.
    * - SpaceX
      - Private
      - X
      - Space exploration and aerospace manufacturer.
    * - Telefonica
      - Public (BME: TEF; NYSE: TEF)
      - X
      - Spanish multinational telecommunications company.
    * - Tesla
      - Public (NASDAQ: TSLA)
      - X
      - Electric vehicle and clean energy company.
    * - Tether
      - Private. 
      - X
      - Cryptocurrency stablecoin issuer (USDT).

* **Vaurum**
* *Details:* Private. Institutional cryptocurrency exchange; rebranded to Xapo (institutional custody).

* **VTB Bank**
* *Details:* Public (MCX: VTBR). Majority state-owned Russian bank.

* **Zasis LLC**
* *Details:* Private. Limited Liability Company associated with Gary Hirst.

-----------
Individuals
-----------

.. list-table::
    :header-rows: 1
    :widths: 15 15 15 55
    
    * - Name
      - Birth Date
      - Birth Country
      - Details
    * - Jeffrey Epstein
      - Jan 20, 1953
      - USA
      - Convicted sex offender and financier. Died Aug 10, 2019.
    * - Steve Bannon
      - Nov 27, 1953
      - USA
      - Media executive, political strategist, and former White House Chief Strategist.
    * - Hector Xavier Monsegur (aka "Sabu")
      - Oct 13, 1983
      - USA 
      - Co-founder of the hacking group LulzSec; became an FBI informant.
    * - Vincenzo Iozzo
      - X
      - Italy
      - Cybersecurity researcher, co-author of *iOS Hacker's Handbook*. Co-founded Iperlane, acquired by CrowdStrike in 2017.
    * - Bobby Kotick
      - 1963
      - USA
      - Former CEO of Activision Blizzard.
    * - Vladimir Putin
      - Oct 7, 1952
      - Russia
      - President of Russia.
    * - Robert Mugabe
      - Feb 21, 1924
      - Zimbabwe 
      - Former President of Zimbabwe. Died 2019.
    * - Bill Clinton
      - Aug 19, 1946
      - USA
      - 42nd President of the United States.
    * - Donald Trump
      - Jun 14, 1946
      - USA
      - 45th President of the United States.
    * - Boris Nikolic
      - X
      - Croatia. 
      - Physician and immunologist; former chief science advisor to Bill Gates. Co-founder of Biomatics Capital.
    * - Martin A. Nowak
      - 1965
      - Austria
      - Professor of Biology and Mathematics at Harvard University; Director of the Program for Evolutionary Dynamics.
    * - George Church
      - Aug 28, 1954
      - USA 
      - Geneticist, molecular engineer, and professor at Harvard Medical School. Pioneer in CRISPR technology.
    * - Rupert Sheldrake
      - Jun 28, 1942
      - UK
      - Biologist and author known for his proposal of "morphic resonance."
    * - Andrea Rossi
      - Jun 3, 1950
      - Italy
      - Entrepreneur and inventor of the E-Cat (Energy Catalyzer), a claimed cold fusion device.
    * - James Clement
      - 1955
      - USA
      - Lawyer, entrepreneur, and transhumanist researcher focused on longevity.
    * - Parijata "Jam" Mackey
      - X
      - X
      - Researcher associated with longevity and transhumanism projects. Mentioned as former management of Androcyte.
    * - Gary Hirst
      - X
      - X
      - Financial executive; associated with Life Extension Foundation; Investor in Androcyte (via Zasis LLC).
    * - Prashant Mali
      - X
      - X
      - Bioengineer and professor at UCSD; expert in CRISPR-Cas9 systems; Co-founder of eGenesisBio.
    * - Luhan Yang
      - X
      - X
      - Biologist and entrepreneur; Chief Scientific Officer at Qihan Biotech.
    * - Kevin Esvelt
      - X
      - X
      - Biologist and professor at MIT Media Lab; inventor of CRISPR-based gene drive technology.
    * - Vatsan Raman, Dan Mandell, Bobby Dhadwar, Eswar Iyer, Rich Terry, Ting Wu, Margo Monroe, Justin Quinn
      - X
      - X
      - Researchers associated with Harvard Medical School, Wyss Institute, or related genomic labs.
    * - Jes Staley
      - Dec 27, 1956
      - USA
      - American banker; former CEO of Barclays and executive at JPMorgan Chase.
    * - Tom Pritzker
      - Jun 6, 1950
      - USA
      - Billionaire businessman; Executive Chairman of Hyatt Hotels Corporation.
    * - Madars Virza
      - X
      - X
      - Research scientist at MIT Media Lab; co-author of the Zerocash protocol.
    * - Brock Pierce
      - Nov 14, 1980
      - USA 
      - Entrepreneur, former child actor, and cryptocurrency advocate (Bitcoin Foundation, Tether).
    * - Larry Summers
      - Nov 30, 1954
      - USA
      - Economist; former US Treasury Secretary and President of Harvard University.
    * - Ehud Barak
      - Feb 12, 1942
      - Israel
      - Former Prime Minister of Israel and Minister of Defense.
    * - Elvira Nabiullina
      - Oct 29, 1963
      - Russia
      - Governor of the Central Bank of Russia.
    * - Sergey Lavrov
      - Mar 21, 1950
      - Russia
      - Foreign Minister of Russia.
    * - Alexei Kudrin
      - Oct 12, 1960
      - Russia
      - Russian economist and politician; former Minister of Finance.
    * - Andrey Kostin
      - Sep 21, 1956
      - Russia
      - President and Chairman of VTB Bank.
    * - Herman Gref
      - Feb 8, 1964
      - USSR
      - CEO of Sberbank; former Russian Minister of Economics and Trade.
    * - Peter Mandelson (Lord Mandelson)
      - Oct 21, 1953
      - UK
      - British Labour politician; former European Trade Commissioner and First Secretary of State.
    * - Michael Lynton
      - Jan 1, 1960
      - UK
      - Business executive; former CEO of Sony Entertainment and Chairman of Snap Inc.
    * - Steven Sinofsky
      - 1965
      - USA
      - Former President of the Windows Division at Microsoft; board partner at Andreessen Horowitz.
    * - David de Rothschild
      - Dec 15, 1942
      - USA
      - French banker; Chairman of Rothschild & Co.
    * - Alessa Staley (aka "Alexa")
      - X
      - USA
      - Daughter of Jes Staley.
    * - Seth Lloyd
      - Aug 2, 1960
      - USA
      - Professor of Mechanical Engineering at MIT; quantum computing researcher.
    * - Murray Gell-Mann
      - Sep 15, 1929
      - USA
      - Physicist and Nobel Laureate (Quarks). Died 2019.
    * - Brian Greene
      - Feb 9, 1963
      - USA
      - Theoretical physicist and mathematician; string theorist.
    * - Leonard Susskind
      - 1940
      - USA
      - Professor of Theoretical Physics at Stanford University.
    * - Lawrence Krauss
      - May 27, 1954
      - USA
      - Theoretical physicist and cosmologist.
    * - Lee Smolin
      - 1955
      - USA
      - Theoretical physicist; faculty at Perimeter Institute for Theoretical Physics.
    * - Elon Musk
      - Jun 28, 1971
      - South Africa
      - CEO of SpaceX and Tesla.
    * - Joscha Bach
      -  1973
      -  Germany
      -  Cognitive scientist and AI researcher.
    * - Steve Hyman
      - 1952
      - USA
      - Neuroscientist; Director of the Stanley Center for Psychiatric Research at the Broad Institute.
    * - Daniel Kahneman
      - Mar 5, 1934
      - Israel
      - Psychologist and Nobel Laureate in Economics.
    * - Misha Gromov
      - Dec 23, 1943
      - Russia
      - Mathematician; Abel Prize laureate known for contributions to geometry.
    * - Noam Chomsky
      - Dec 7, 1928
      - USA
      - Linguist, philosopher, and cognitive scientist.
    * - Valeria Wasserman
      - X
      - 
      - Translator and legal specialist; married Noam Chomsky in 2014.
    * - Darren Indyke
      - X
      - X
      - Lawyer; longtime legal counsel for Jeffrey Epstein.
    * - Richard Kahn
      - X
      - X
      - Accountant; longtime accountant for Jeffrey Epstein.
    * - Karyna Shuliak
      - 1989
      - Belarus
      - Dentist; identified as Epstein's girlfriend at the time of his death.