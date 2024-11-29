<?php
// Vérifier si la méthode est bien POST
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Nom du fichier où les données seront enregistrées
    $filename = 'save.txt';

    // Ouvrir le fichier en mode 'a' pour ajouter les données sans écraser le contenu existant
    $file = fopen($filename, 'a');

    if ($file) {
        // Écrire toutes les données de $_POST dans le fichier
        fwrite($file, "=== Nouvelle soumission ===\n");
        fwrite($file, print_r($_POST, true)); // Utilisation de print_r pour afficher toutes les données
        fwrite($file, "\n\n");

        // Fermer le fichier
        fclose($file);

        echo "Les données ont été enregistrées avec succès.";
    } else {
        echo "Erreur lors de l'ouverture du fichier.";
    }
} else {
    echo "Aucune donnée POST reçue.";
}
?>

