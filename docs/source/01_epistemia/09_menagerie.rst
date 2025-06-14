.. _menagerie:

Menagerie
=========

.. _holy-c:

-----
HolyC
-----

.. collapse:: First Person Shooter

    .. code-block:: c

        //$FG,2$Set snap to 4 and width to 4$FG$
        //$FG,2$if you edit this map.$FG$

        //$FG,2$Don't forget to change the$FG$
        //$FG,2$starting position.$FG$

        $PI,"<1>",1$

        #define SCREEN_SCALE                512
        #define PLOT_GRID_WIDTH                24
        #define PLOT_GRID_HEIGHT        24

        #define MAP_SCALE        4
        I8 map_width,map_height;
        I1 *map=NULL,
            *panels_processed_bitmap=NULL;

        I8 man_xx,man_yy;
        double man_theta;

        void FPSTransform(GrBitMap *base,I8 *x,I8 *y,I8 *z)
        {
        GrRotate(base->r,x,y,z);
        *x=SCREEN_SCALE/2* *x/(AbsI8(SCREEN_SCALE-*z)+1);
        *y=SCREEN_SCALE/2* *y/(AbsI8(SCREEN_SCALE-*z)+1);
        *x+=base->x;
        *y+=base->y;
        *z=base->z-*z;
        }

        void LOSPlot(BoolI8 *result,I8 x,I8 y,I8 z)
        {
        nounusedwarn z;
        if (!map[y*map_width+x])
            *result=FALSE;
        }

        BoolI8 LOS(I8 x1,I8 y1,I8 x2,I8 y2)
        { //$FG,2$Line of sight$FG$
        BoolI8 result=TRUE;
        Line(&result,x1,y1,0,x2,y2,0,&LOSPlot);
        return result;
        }

        void UpdateWin(TssStruct *tss)
        {
        GrBitMap *base=GrAlias(grbase,tss);
        I8 i,j,*r1,*r2,*s2w,xx,yy,x,y,
                x1w,y1w,x1h,y1h,xh,yh,zh,
                cx=tss->win_pixel_width/2,
                cy=tss->win_pixel_height/2;
        P3I4 t[4];
        GrAllocDepthBuffer(base);
        MemSet(panels_processed_bitmap,0,(map_width*map_height+7)>>3);

        //$FG,2$World to screen$FG$
        Free(base->r);
        r1=GrRotZ(man_theta-pi/2,tss);
        r2=GrRotX(80*2*pi/360,tss);
        base->r=GrMulMat(r2,r1,tss);
        Free(r1);
        Free(r2);

        xh=-man_xx/SCREEN_SCALE; yh=-man_yy/SCREEN_SCALE; zh=0;
        GrRotate(base->r,&xh,&yh,&zh);
        GrSetTranslation(base->r,xh,yh,zh);

        //$FG,2$Screen to world$FG$
        r1=GrRotZ(-man_theta+pi/2,tss);
        r2=GrRotX(-80*2*pi/360,tss);
        s2w=GrMulMat(r1,r2,tss);

        xh=0; yh=0; zh=-SCREEN_SCALE;
        GrRotate(s2w,&xh,&yh,&zh);
        Free(r1);
        Free(r2);

        base->x=cx;
        base->y=cy;
        base->z=SCREEN_SCALE/8;
        base->flags|=BMF_TRANSFORMATION;
        base->transform=&FPSTransform;

        x1h=man_xx+yh*PLOT_GRID_WIDTH/2+xh*PLOT_GRID_HEIGHT;
        y1h=man_yy-xh*PLOT_GRID_WIDTH/2+yh*PLOT_GRID_HEIGHT;
        xh>>=1; yh>>=1;
        for (j=0;j<PLOT_GRID_HEIGHT*2;j++) {
            x1w=x1h;
            y1w=y1h;
            for (i=0;i<PLOT_GRID_WIDTH*4;i++) {
                xx=x1w/SCREEN_SCALE; yy=y1w/SCREEN_SCALE;
                x=xx*SCREEN_SCALE-man_xx; y=yy*SCREEN_SCALE-man_yy;
                if (1<=xx<map_width-1 && 1<=yy<map_height-1 &&
                        !Bts(panels_processed_bitmap,yy*map_width+xx)) {
                    if ((base->color=map[yy*map_width+xx]) &&
        LOS(xx,yy,man_xx/SCREEN_SCALE,man_yy/SCREEN_SCALE)) {
                        t[0].x=x;
                        t[0].y=y;
                        t[0].z=0;
                        t[1].x=x+SCREEN_SCALE;
                        t[1].y=y;
                        t[1].z=0;
                        t[2].x=x+SCREEN_SCALE;
                        t[2].y=y+SCREEN_SCALE;
                        t[2].z=0;
                        t[3].x=x;
                        t[3].y=y+SCREEN_SCALE;
                        t[3].z=0;
                        GrFillPolygon3(base,4,t);
                        if (!map[(yy+1)*map_width+xx]) {
                            base->color=WHITE;
                            t[0].x=x;
                            t[0].y=y+SCREEN_SCALE;
                            t[0].z=0;
                            t[1].x=x+SCREEN_SCALE;
                            t[1].y=y+SCREEN_SCALE;
                            t[1].z=0;
                            t[2].x=x+SCREEN_SCALE;
                            t[2].y=y+SCREEN_SCALE;
                            t[2].z=SCREEN_SCALE;
                            t[3].x=x;
                            t[3].y=y+SCREEN_SCALE;
                            t[3].z=SCREEN_SCALE;
                            GrFillPolygon3(base,4,t);
                        }
                        if (!map[yy*map_width+xx+1]) {
                            base->color=YELLOW;
                            t[0].x=x+SCREEN_SCALE;
                            t[0].y=y;
                            t[0].z=0;
                            t[1].x=x+SCREEN_SCALE;
                            t[1].y=y+SCREEN_SCALE;
                            t[1].z=0;
                            t[2].x=x+SCREEN_SCALE;
                            t[2].y=y+SCREEN_SCALE;
                            t[2].z=SCREEN_SCALE;
                            t[3].x=x+SCREEN_SCALE;
                            t[3].y=y;
                            t[3].z=SCREEN_SCALE;
                            GrFillPolygon3(base,4,t);
                        }
                        if (!map[(yy-1)*map_width+xx]) {
                            base->color=WHITE;
                            t[0].x=x;
                            t[0].y=y;
                            t[0].z=0;
                            t[1].x=x+SCREEN_SCALE;
                            t[1].y=y;
                            t[1].z=0;
                            t[2].x=x+SCREEN_SCALE;
                            t[2].y=y;
                            t[2].z=SCREEN_SCALE;
                            t[3].x=x;
                            t[3].y=y;
                            t[3].z=SCREEN_SCALE;
                            GrFillPolygon3(base,4,t);
                        }
                        if (!map[yy*map_width+xx-1]) {
                            base->color=YELLOW;
                            t[0].x=x;
                            t[0].y=y;
                            t[0].z=0;
                            t[1].x=x;
                            t[1].y=y+SCREEN_SCALE;
                            t[1].z=0;
                            t[2].x=x;
                            t[2].y=y+SCREEN_SCALE;
                            t[2].z=SCREEN_SCALE;
                            t[3].x=x;
                            t[3].y=y;
                            t[3].z=SCREEN_SCALE;
                            GrFillPolygon3(base,4,t);
                        }
                    }
                }
                x1w-=yh;
                y1w+=xh;
            }
            x1h-=xh;
            y1h-=yh;
        }
        Free(s2w);
        base->color=LTGREEN;
        GrLine(base,cx-5,cy,cx+5,cy);
        GrLine(base,cx,cy-5,cx,cy+5);

        GrDel(base);
        }


        void Init()
        {
        I8 x,y,minx,maxx,miny,maxy;
        GrBitMap *base;
        GrElemsExtents($IB,"<1>",1$,&minx,&maxx,&miny,&maxy);
        map_width =(maxx-minx+1)/MAP_SCALE+2;
        map_height=(maxy-miny+1)/MAP_SCALE+2;
        Free(map);
        Free(panels_processed_bitmap);
        map=MAllocZ(map_width*map_height*sizeof(I1));
        panels_processed_bitmap=MAlloc((map_width*map_height+7)>>3);
        base=GrNew(BMT_COLOR4,map_width*MAP_SCALE,map_height*MAP_SCALE);
        GrElemsPlot(base,-minx+MAP_SCALE,-miny+MAP_SCALE,0,$IB,"<1>",1$);
        for (y=1;y<map_height-1;y++)
            for (x=1;x<map_width-1;x++)
                    map[y*map_width+x]=GrPeek(base,x*MAP_SCALE,y*MAP_SCALE);
        GrDel(base);
        man_xx=2*SCREEN_SCALE;
        man_yy=5.5*SCREEN_SCALE;
        man_theta=0;
        }

        void CleanUp()
        {
        Free(map);
        Free(panels_processed_bitmap);
        map=NULL;
        panels_processed_bitmap=NULL;
        }

        void FPS()
        {
        I8 c,p1,p2,ch,sc,x,y,step;
        void old_update=Fs->update_win;
        U8 old_text_attr=Fs->text_attr;

        WinMax;
        Init;
        Fs->text_attr=WHITE+BLACK<<4;

        //$FG,2$The text layer under the graphics lags a frame$FG$
        //$FG,2$therefore the fill operations screw-up without this.$FG$
        ClearWinText;

        Fs->update_win=&UpdateWin;
        do {
            Init;
            ch=0;
            do {
                while (c=ScanMsg(&p1,&p2,1<<MSG_KEY_DOWN|1<<MSG_KEY_UP)) {
                    ch=p1; sc=p2;
                    if (c==MSG_KEY_DOWN) {
                        switch (sc.u1[0]) {
                            case SC_CURSOR_RIGHT:
                                man_theta-=pi/32;
                                break;
                            case SC_CURSOR_LEFT:
                                man_theta+=pi/32;
                                break;
                            case SC_CURSOR_UP:
                                step=SCREEN_SCALE/2;
                                do {
                                    x=man_xx+step*Cos(man_theta);
                                    y=man_yy-step*Sin(man_theta);
                                    x=Limit(x,0,map_width*SCREEN_SCALE);
                                    y=Limit(y,0,map_height*SCREEN_SCALE);
                                    if (map[y/SCREEN_SCALE*map_width+x/SCREEN_SCALE]==RED) {
                                        man_xx=x;
                                        man_yy=y;
                                        break;
                                    } else
                                        step>>=1;
                                } while (step);
                                break;
                            case SC_CURSOR_DOWN:
                                step=SCREEN_SCALE/2;
                                do {
                                    x=man_xx-step*Cos(man_theta);
                                    y=man_yy+step*Sin(man_theta);
                                    x=Limit(x,0,map_width*SCREEN_SCALE);
                                    y=Limit(y,0,map_height*SCREEN_SCALE);
                                    if (map[y/SCREEN_SCALE*map_width+x/SCREEN_SCALE]==RED) {
                                        man_xx=x;
                                        man_yy=y;
                                        break;
                                    } else
                                        step>>=1;
                                } while (step);
                                break;
                        }
                    }
                }
                WinSync; //$FG,2$msgs are only queued by winmngr$FG$
            } while (ch!=CH_ESC && ch!=CH_CR && ch!=CH_CTRLQ);
        } while (ch!=CH_ESC && ch!=CH_CTRLQ);

        Sound(0);
        Fs->update_win=old_update;
        Fs->text_attr=old_text_attr;
        CleanUp;
        }


        FPS;

.. _terryology:

----------
Terryology
----------

- `One Times One Equals Two <https://tcotlc.com>`_
    - :download:`OTOET PDF <../_static/pdf/otoet.pdf>`

.. image:: ../_static/img/context/psychological/flower-of-life.png
   :width: 70%
   :alt: The Flower Of Life
   :align: center

.. image:: ../_static/img/context/psychological/terryology-syllogism.png
   :width: 70%
   :alt: The Walter Russell Periodic Table
   :align: center

.. collapse:: Mathematics 101
        
    .. epigraph::

        MATHEMATICS 101

        1 x 1 = 1
        
        Or so we've been taught.
        
        We were taught around this very impressionable time that Santa
        Claus and the Easter Bunny were also real. Yet, over the next few
        years we ultimately came to terms with the fact that our chimneys
        were far to narrow for a jolly old fellow to climb down. Also, we re-
        luctantly accepted the fact that reindeer (elk) do not fly nor do rab-
        bits lay eggs. Thus, we matured and abandoned fairytales and the
        need for the improbable or impossible to explain the world that we
        live in and our Universe. A child for his part is gullible, therefore
        he or she can be easily encouraged to believe almost anything that
        is presented to them without demanding the need for proof. Espe-
        cially, if it is being presented by someone that they trust and view
        as an authority. In like manner, the notion that 1 x 1 = 1 was drilled
        into our young, impressionable minds at a time when we were very
        susceptible to suggestion. At a stage in our development before we
        could begin to grasp the importance of questioning the accuracy of
        the lessons being taught.
        
        In stark contrast, the mind of a mature and modestly educated
        adult must be won over with strong and convincing argument. An
        argument that is based upon observed natural phenomena, coupled
        with concrete evidence and irrefutable fact. Every adult is responsi-
        ble for his/her beliefs and is equally responsible for the ideas that
        he or she propagates into this world. Never forget, “Every action has
        an equal and opposite reaction.” How much more shall we be held
        accountable for an ideology that will forever affect how we measure
        our Universe and All Things within it?
        
        Therefore, I challenge the narrative that 1 x 1 = 1.
        
        I believe that 1 x 1 = 2.

        Why? Because:

        To Multiply means
        to make many or manifold.
        
        It means, to increase in number or quantity.
        
        Therefore, it must increase in size and quantity or it is not multipli-
        cation. This is the undisputed definition of the word:
        
        TO MULTIPLY
        
        You couldn't ask for a more simple and concise definition of a word.
        Consequently, 1 x 1 = (ing) 1 could never be a part of the “multipli-
        cation table” because it fails to satisfy the definition of the term, "to
        increase in number". 1 x 1 = (ing) 1 sounds more like a philosophical
        assertion, like Shakespeare's, “To be, or Not to be, that is the ques-
        tion” rather than a function of multiplication or mathematics.
        It should be obvious that 1 x 1 cannot equal 1 by reason of the very
        definition of the term to “multiply”.
        
        Nevertheless, something tells me you're going need a little more
        convincing than just the true definition of a word or the Unbal-
        anced Equation Argument, the irregularities of The Identity Ele-
        ment which could also be called the Jim Crow Laws of Mathematics
        and the 2-D Unreality Argument to change your minds concerning
        this deeply ingrained philosophy. After all, our entire world econo-
        my seems hinged upon this idea. What will it take to convince this
        generation that we are at least 6,000 years down a darkening path
        going the wrong way, completely blind to the truth? What possible
        argument is there to help Man finally step out of the darkness and
        into the light?

        Let's consider this: Multiplication is a mathematical operation which
        is governed by two laws:

        The Commutative Law and the Associative Law, symbolized by
        (a x b), (a . b), (a * b), or (ab), and signifying, when (a) and (b) are
        positive integers, that (a) is to be ADDED to itself as many times as
        there are units in (b); the ADDITION of a number to itself as often
        as is indicated by another number.
        
        By interpretation of the aforementioned laws along with application
        of those said laws we have clear and rational proof that
        1 x 1 = 2.
        
        If it wasn't for the Identity Property, a property that calls for
        the immediate suspension of the first, second and third laws of
        motion. What is more reasonable, to question all observable
        physical phenomena or to question an arbitrary rule called the
        “Identity Property”?
        Think about it, out of all of the geniuses who have roamed this
        planet throughout the history of the world, not one of them have
        ever observed in natural phenomena an example of 1 x 1 =(ing) 1.
        Because Nature does not subscribe to Man's mathematics. What is
        even more surprising is that no other thinking human being out
        of all the people who ever lived and observed natural phenomena,
        that not one of them has ever publicly questioned 1 x 1 = (ing) 1.
        The Pythagoreans might have questioned “irrational numbers” but
        they never publicly questioned the notion that 1 x 1 (should be)= (to
        more than) 1.

        That's unfortunate, so it must stand to reason that this flawed equa-
        tion must have been indoctrinated into our minds before our ability
        to discern truth from fiction.
        
        -- Terrence DaShon Howard

.. _time-cube:

---------
Time Cube
---------

.. image:: ../_static/svg/time-cube.svg
   :width: 70%
   :alt: The Time Cube
   :align: center

.. _walter-russell-periodic-table:

-----------------------------
Walter Russell Periodic Table
-----------------------------

.. image:: ../_static/img/context/psychological/walter-russel-periodic-table.png
   :width: 70%
   :alt: The Walter Russell Periodic Table
   :align: center