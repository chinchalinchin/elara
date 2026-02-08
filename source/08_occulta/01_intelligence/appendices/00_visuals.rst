.. _intelligence-appendix-i-visuals:

-------------------
Appendix I: Visuals
-------------------

.. note::

  Click to zoom in on diagrams and drag to explore.

**Epstein's Network**

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
