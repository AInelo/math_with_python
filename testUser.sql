psql -h localhost -U toli8447_lionel -d toli8447_comptaplan


------------------------- Official -------------------------------------

INSERT INTO users (firstname, lastname, email, password, country_code, numero_tel, date_inscription, date_paiement, status_paiement, duree_abonnement, amount_to_pay, user_category, type_user)
VALUES
('Abonnee', 'USER', 'user-abonnee@gmail.com', '$2b$10$avfInxCAPcG0wn0ZLs49l.ZL1d5/3H0Zfo241z3RS02Q2Sklc0DrS', '229' ,'96769716', '2024-01-02', '2024-02-02', true, 365, 15000 ,'entreprise', 'simple');

INSERT INTO users (firstname, lastname, email, password, country_code, numero_tel, date_inscription, date_paiement, status_paiement, duree_abonnement, amount_to_pay, user_category, type_user)
VALUES
('NonAbonnee', 'USER', 'user-non-abonnee@gmail.com', '$2b$10$avfInxCAPcG0wn0ZLs49l.ZL1d5/3H0Zfo241z3RS02Q2Sklc0DrS', '229' ,'96769716', '2024-01-02', null, false, 0, 4500 ,'etudiant', 'simple');


------------------------- Official -------------------------------------

Utilisateur 1 : 
INSERT INTO users (firstname, lastname, email, password, country_code, numero_tel, date_inscription, date_paiement, status_paiement, duree_abonnement, amount_to_pay, user_category, type_user)
VALUES
('Abonnee', 'USER1', 'user1-tampon-abonnee@gmail.com', '$2b$10$avfInxCAPcG0wn0ZLs49l.ZL1d5/3H0Zfo241z3RS02Q2Sklc0DrS', '229' ,'96000000', '2024-01-02', '2024-02-02', true, 365, 15000 ,'entreprise', 'simple');


Utilisateur 2 : 
INSERT INTO users (firstname, lastname, email, password, country_code, numero_tel, date_inscription, date_paiement, status_paiement, duree_abonnement, amount_to_pay, user_category, type_user)
VALUES
('Abonnee', 'USER2', 'user2-tampon-abonnee@gmail.com', '$2b$10$avfInxCAPcG0wn0ZLs49l.ZL1d5/3H0Zfo241z3RS02Q2Sklc0DrS', '229' ,'96000000', '2024-01-02', '2024-02-02', true, 365, 15000 ,'entreprise', 'simple');


Utilisateur 3 : 
INSERT INTO users (firstname, lastname, email, password, country_code, numero_tel, date_inscription, date_paiement, status_paiement, duree_abonnement, amount_to_pay, user_category, type_user)
VALUES
('Abonnee', 'USER3', 'user3-tampon-abonnee@gmail.com', '$2b$10$avfInxCAPcG0wn0ZLs49l.ZL1d5/3H0Zfo241z3RS02Q2Sklc0DrS', '229' ,'96000000', '2024-01-02', '2024-02-02', true, 365, 15000 ,'entreprise', 'simple');
