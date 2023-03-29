-- trigger si nom utilisateur nouveau ajouter dans base de données sinon rajouter +1 pour partie jouer


Create Table public."joueur"(
    id_joueur integer not null,
    nom_joueur text,
    nb_Partie integer,
    mise_depart integer
);

insert into joueur values (1,'toto',4,100);
insert into joueur values (2,'robot',2,100);

create table public."partie"(
    id_Partie integer not null,
    id_joueur integer,
    victoire text
);

insert into partie values (1,2,'True');

create table public."ia"(
    niveau_IA text,
    id_Partie integer not null,
    id_joueur integer not null,
    victoire text
);

insert into ia values ('facile',1,2,'True');

create table public."humain"(
    id_Partie integer not null,
    id_joueur integer not null,
    victoire text
);

insert into humain values (1,1,'false');

create table public."avoir_resultat_match"(
    id_Partie integer not null,
    id_joueur integer not null,
    victoire text,
    main_gagnante text,
    gains_final integer,
    nb_coucher integer

);

insert into avoir_resultat_match values (1,1,'true','brelan',200,0);

create or replace function joueur_coucher()
returns void as $$

declare 
-- curseur
joueur_coucher_curseur cursor for select j.nom_joueur,count(nb_coucher), arm.id_Partie
from joueur j inner join avoir_resultat_match arm 
on j.id_joueur = arm.id_joueur
GROUP by j.nom_joueur,nb_coucher, arm.id_Partie;

--  variable
v_nom joueur.nom_joueur%type;
v_coucher avoir_resultat_match.nb_coucher%type;
v_idPartie avoir_resultat_match.id_Partie%type;


begin
open joueur_coucher_curseur;
loop
    fetch joueur_coucher_curseur into v_nom, v_coucher,v_idPartie;
    exit when not found;
    raise notice "Le joueur % s'est couché % durant la partie %", v_nom, v_coucher, v_idPartie;
end loop;
close joueur_coucher_curseur;
end;
$$ language plpgsql;


create or replace function meilleurjoueur()
returns void as $$

declare
v_victoire avoir_resultat_match.victoire%type;
v_idPartie avoir_resultat_match.id_Partie%type;
v_nom Joueur.nom_joueur%type;
v_idJoueur Joueur.id_joueur%type;
v_info_joueur

meilleurjoueur_curseur cursor for select j.nom_joueur, count(arm.victoire) from joueur j
inner join avoir_resultat_match arm 
on j.id_joueur = arm.id_joueur
where v_victoire like 'true'
GROUP BY j.nom_joueur, arm.victoire;

begin 
open meilleurjoueur_curseur;
    loop
    fetch meilleurjoueur_curseur into v_nom,v_victoire;
    exit when not found;
    raise notice "le meilleur joueur est % avec % victoires",v_nom,v_victoire;
    end loop;
close meilleurjoueur_curseur;
end;
$$ language plpgsql;

create or replace function ajouter_joueur(v_joueur_nom varchar,v_mise_depart int)
returns trigger as $$

declare

joueur_Partie joueur.nom_joueur%rowtype;
liste_joueur_curseur cursor for select id_joueur,count(nb_Partie) from joueur;
begin

open liste_joueur_curseur;
insert into Joueur values (new.id_joueur,v_joueur_nom,new.nb_Partie,v_mise_depart);
loop
fetch liste_joueur_curseur into joueur_Partie;
exit when not found;

if joueur_Partie.id <> new.id_joueur then
    insert into Joueur values (joueur_Partie.id,v_joueur_nom,joueur_Partie.nb_Partie+1,v_mise_depart);
    -- insert into Joueur values (new.typ_id,vtype,1);
end if;
end loop;
close liste_joueur_curseur;
end; 
$$ language plpgsql;










-- -------------------------------------------

create or replace function probabilite_victoire(id_joueur1 int, id_joueur2 int)
returns void as $$

declare
joueur1_id avoir_resultat_match%rowtype;
joueur2_id avoir_resultat_match%rowtype;

curseur_joueur1 cursor for select p.id_partie, j.id_joueur, arm.victoire, j.nom_joueur from joueur j
inner join avoir_resultat_match arm on j.id_joueur = arm.id_joueur
inner join partie p on arm.id_partie = p.id_partie
where j.id_joueur = id_joueur1;

curseur_joueur2 cursor for select p.id_partie, j.id_joueur, arm.victoire,j.nom_joueur from joueur j
inner join avoir_resultat_match arm on j.id_joueur = arm.id_joueur
inner join partie p on arm.id_partie = p.id_partie
where j.id_joueur = id_joueur2;

begin 
    open curseur_joueur1;
    loop
        fetch curseur_joueur1 into joueur1_id;
        exit when not found;
    
    open curseur_joueur2;
    loop 
        fetch curseur_joueur2 into joueur2_id;
        exit when not found;

    if (joueur1_id.id_partie == joueur2_id.id_match) then
        if (joueur1_id.victoire == joueur2_id.victoire) then

        raise notice 'Le joueur % est a égalité avec le joueur %',joueur1_id.nom_joueur,joueur1_id.nom_joueur;

        if (joueur1_id.victoire == 1) then
         raise notice 'Le joueur % a gagné la partie',joueur1_id.nom_joueur;

        else 
        raise notice 'Le joueur % a gagné la partie',joueur2_id.nom_joueur;

        end if;
    end if;
    end loop;
    end loop;
    close curseur_joueur1;
    close curseur_joueur2;
end;
$$ language plpgsql;



create or replace function increment_partie()
returns trigger as $$
