# DeepSeek CLI 🚀

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-API-green)](https://platform.deepseek.com)

Un CLI intelligent et adaptable pour l'API DeepSeek, conçu pour les développeurs modernes.

## ✨ Features

- 🤖 **Assistant IA contextuel** - S'adapte automatiquement à votre stack technique
- 💾 **Cache intelligent** - Réponses plus rapides, coûts réduits
- 📁 **Gestion multi-fichiers** - Analysez plusieurs fichiers simultanément
- 🔧 **Refactoring intelligent** - Améliorez votre code automatiquement
- 🌐 **Multi-langages** - TypeScript, Python, Rust, Go, et plus encore
- ⚡ **Installation simple** - Disponible via pip

## 🚀 Installation

### Via pip (recommandé)
```bash
pip install deepseek-cli
```

### Depuis les sources
```bash
git clone https://github.com/FDumusois/DeepSeekCLI.git
cd DeepSeekCLI
pip install -e .
```

## ⚡ Utilisation Rapide

### Configuration
```bash
# Configurez votre clé API (obtenez-la sur https://platform.deepseek.com)
export DEEPSEEK_API_KEY="votre_cle_api"
```

### Commandes de base
```bash
# Génération de code
deepseek "Crée une fonction Python pour trier un dictionnaire"

# Analyse de fichiers
deepseek --file mon_script.py "Optimise les performances de ce code"

# Refactoring multi-fichiers
deepseek --files utils.ts,types.ts "Refactorise vers TypeScript moderne"

# Debuggage intelligent
deepseek --file error.log "Analyse cette erreur et propose un correctif"
```

## 🛠️ Exemples Avancés

### Développement TypeScript/React
```bash
# Création de composants
deepseek "Crée un composant React TypeScript avec hooks et props typées"

# Refactoring de code existant
deepseek --file component.tsx "Convertir ce composant en utilisant React.memo"

# Optimisation de performances
deepseek --files hooks.ts,utils.ts "Détecte les bottlenecks de performance"
```

### Développement Python
```bash
# Création d'APIs
deepseek "Crée une API FastAPI avec validation Pydantic"

# Scripts d'automatisation
deepseek "Écris un script Python pour cleaner un dossier temporaire"

# Analyse de données
deepseek --file analysis.py "Optimise ce code Pandas pour de gros datasets"
```

### Gestion de projet
```bash
# Setup de projet
deepseek "Crée la structure pour un projet Next.js avec TypeScript et Tailwind"

# Configuration
deepseek "Génère un docker-compose.yml pour une app React + Node.js"

# Documentation
deepseek --file api.js "Génère la documentation JSDoc pour cette API"
```

## ⚙️ Arguments CLI Complets

```bash
deepseek "votre prompt" [OPTIONS]

Options:
  -f, --file FICHIER        Fichier à inclure dans le contexte
  --files FICHIERS          Liste de fichiers séparés par des virgules
  --no-cache               Désactiver le cache pour cette requête
  -o, --output FICHIER      Sauvegarder la réponse dans un fichier
  --temperature NUMBER     Contrôle la créativité (0.1-1.0, défaut: 0.1)
  --model MODEL            Modèle DeepSeek à utiliser (défaut: deepseek-coder)
  --help                   Afficher l'aide complète
```

## 🔧 Configuration Avancée

### Variables d'environnement
```bash
export DEEPSEEK_API_KEY="votre_cle"          # Requis
export DEEPSEEK_MODEL="deepseek-coder"       # Optionnel
export DEEPSEEK_BASE_URL="https://api.deepseek.com"  # Optionnel
export DEEPSEEK_CACHE_DIR="~/.cache/deepseek" # Optionnel
```

### Fichier de configuration
Créez `~/.config/deepseek/config.json` :
```json
{
  "api_key": "votre_cle_api",
  "model": "deepseek-coder",
  "temperature": 0.1,
  "cache_enabled": true,
  "auto_apply": false
}
```

## 🏗️ Architecture Technique

### Détection Automatique du Contexte
Le CLI analyse automatiquement :
- **Extensions de fichiers** (.ts, .py, .rs, etc.)
- **Structure de projet** (package.json, requirements.txt, etc.)
- **Patterns de code** (hooks React, classes Python, etc.)

### Cache Intelligent
- **Hachage des requêtes** pour éviter les appels API duplicates
- **Stockage local** dans `~/.cache/deepseek`
- **Expiration automatique** après 7 jours

### Gestion d'Erreurs Robuste
- **Retry automatique** sur les erreurs réseau
- **Fallback models** si le modèle principal échoue
- **Messages d'erreur clairs** et actionnables

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment aider :

### Rapporter un Bug
1. Allez dans [Issues](https://github.com/FDumusois/DeepSeekCLI/issues)
2. Créez une nouvelle issue avec le template "Bug Report"
3. Décrivez le problème en détail

### Proposer une Fonctionnalité
1. Ouvrez une issue avec le template "Feature Request"
2. Décrivez l'idée et son utilité
3. Discutons-en ensemble !

### Développement
```bash
# Setup de l'environnement
git clone https://github.com/FDumusois/DeepSeekCLI.git
cd DeepSeekCLI
pip install -e ".[dev]"

# Lancer les tests
pytest tests/

# Vérifier le code
flake8 deepseek_cli.py
```

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

## 📊 Roadmap

### Version 1.0.0
- [x] CLI basique avec cache
- [x] Support multi-fichiers
- [x] Installation via pip
- [ ] Mode conversationnel
- [ ] Templates de projets

### Version 2.0.0
- [ ] Extension VS Code
- [ ] Integration Git intelligente
- [ ] Plugins personnalisables
- [ ] Analytics d'usage anonymes

## ❓ FAQ

### Où obtenir une clé API DeepSeek ?
Visitez [platform.deepseek.com](https://platform.deepseek.com) pour créer un compte et obtenir votre clé API gratuite.

### Le cache fonctionne comment ?
Le CLI hash votre prompt et les fichiers inclus. Les réponses identiques sont servies depuis le cache local, réduisant les coûts et améliorant les performances.

### Puis-je utiliser d'autres modèles AI ?
Actuellement, seul DeepSeek est supporté. L'architecture est conçue pour permettre l'ajout d'autres providers à l'avenir.

### Comment désactiver le cache ?
Utilisez l'option `--no-cache` ou définissez `DEEPSEEK_CACHE_ENABLED=false`.

## 📄 Licence

Ce projet est sous licence Apache 2.0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Frédéric Dumusois**
- GitHub: [@FDumusois](https://github.com/FDumusois)
- Projet: [DeepSeekCLI](https://github.com/FDumusois/DeepSeekCLI)

## 🙏 Remerciements

- [DeepSeek AI](https://www.deepseek.com) pour leur excellente API
- La communauté open source pour l'inspiration
- Tous les contributeurs qui aident à améliorer ce projet

## ⚠️ Disclaimer

Ce projet n'est pas affilié à DeepSeek AI. Vous avez besoin d'une clé API valide de [platform.deepseek.com](https://platform.deepseek.com). L'utilisation de l'API DeepSeek est soumise à leurs conditions d'utilisation.