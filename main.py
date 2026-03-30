from app.ui.tela_principal import iniciar_interface
from app.database.db import criar_tabela

if __name__ == "__main__":
    criar_tabela()
    iniciar_interface()