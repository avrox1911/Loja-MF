import customtkinter as ct
import tkinter as tk
from tkinter import messagebox
import psycopg2
 
# Carregar tema personalizado
ct.ThemeManager.load_theme("custom_theme.json")

# Definir o modo de aparência (claro ou escuro)
ct.set_appearance_mode("dark")  # ou "light"

# Função para alternar entre modo claro e escuro
def toggle_mode():
    current_mode = ct.get_appearance_mode().lower()  # Converte para minúsculas
    if current_mode == "dark":
        ct.set_appearance_mode("light")
    else:
        ct.set_appearance_mode("dark")

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="loja_MF",
            user="postgres",
            password="milla1207",
            options="-c client_encoding=UTF8"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

#### Classe principal do aplicativo ###
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Form Example")
        self.title("Banco de dados - Loja MF")
        self.geometry("1000x600")

        # Barra de menu
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        
        # Menu de Arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Menu de Formulário
        self.form_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.form_menu.add_command(label="Cadastrar", command=lambda: self.show_form("cadastro"))
        self.form_menu.add_command(label="Consultar", command=lambda: self.show_form("consulta"))
        self.form_menu.add_command(label="Agenda", command=lambda: self.show_form("agenda"))
        self.menu_bar.add_cascade(label="Formulário", menu=self.form_menu)
        
        # Menu Sobre
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="Sobre", command=lambda: self.show_form("sobre"))
        self.menu_bar.add_cascade(label="Sobre", menu=self.about_menu)
        
        # Frame principal
        self.form_frame = ct.CTkFrame(self, corner_radius=10)
        self.form_frame.pack(side="top", padx=5, pady=5, fill="both")
        
        # Botões principais
        self.cad_button = ct.CTkButton(self.form_frame, text="Cadastrar", command=lambda: self.show_form("cadastro"))
        self.cad_button.grid(row=0, column=0, padx=5, pady=5)
        self.con_button = ct.CTkButton(self.form_frame, text="Consultar", command=lambda: self.show_form("consulta"))
        self.con_button.grid(row=0, column=1, padx=5, pady=5)
        self.agenda_button = ct.CTkButton(self.form_frame, text="Agenda", command=lambda: self.show_form("agenda"))
        self.agenda_button.grid(row=0, column=2, padx=5, pady=5)

        ### Botão para alternar entre modo claro e escuro ###
        self.toggle_button = ct.CTkButton(self.form_frame, text="Alternar Modo", command=toggle_mode)
        self.toggle_button.grid(row=0, column=3, padx=395, pady=5)

        ### Criação dos formulários ###
        self.create_form_cadastro()
        self.create_form_consulta()
        # self.create_form_agenda()
        
        ### Esconder os formulários inicialmente ###
        self.form_cadastro.pack_forget()
        self.form_consulta.pack_forget()
        # self.form_agenda.pack_forget()

    # Função para criar o formulário de cadastro
    def create_form_cadastro(self):

        self.form_cadastro = ct.CTkFrame(self, corner_radius=10)

        # Função de validação
        validate_cmd = self.register(self.validate_entry)
        
        # Nome
        self.name_label = ct.CTkLabel(self.form_cadastro, text="Nome:")
        self.name_label.grid(row=0, column=0, pady=10)
        self.name_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.name_entry.grid(row=0, column=1, pady=10)
        
        # RG
        self.rg_label = ct.CTkLabel(self.form_cadastro, text="RG:")
        self.rg_label.grid(row=1, column=0, padx=10, pady=10)
        self.rg_entry = ct.CTkEntry(self.form_cadastro, width=200, validate="key", validatecommand=(validate_cmd, '%P', '9'))
        self.rg_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # CPF
        self.cpf_label = ct.CTkLabel(self.form_cadastro, text="CPF:")
        self.cpf_label.grid(row=2, column=0, padx=10, pady=10)
        self.cpf_entry = ct.CTkEntry(self.form_cadastro, width=200, validate="key", validatecommand=(validate_cmd, '%P', '11'))
        self.cpf_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # E-mail
        self.email_label = ct.CTkLabel(self.form_cadastro, text="E-mail:")
        self.email_label.grid(row=3, column=0, padx=10, pady=10)
        self.email_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10)
        
        # Telefone
        self.telefone_label = ct.CTkLabel(self.form_cadastro, text="Telefone:")
        self.telefone_label.grid(row=4, column=0, padx=10, pady=10)
        self.telefone_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.telefone_entry.grid(row=4, column=1, padx=10, pady=10)
        
        # Endereço
        self.endereco_label = ct.CTkLabel(self.form_cadastro, text="Endereço:")
        self.endereco_label.grid(row=5, column=0, padx=10, pady=10)
        self.endereco_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.endereco_entry.grid(row=5, column=1, padx=10, pady=10)
        
        # CEP
        self.cep_label = ct.CTkLabel(self.form_cadastro, text="CEP:")
        self.cep_label.grid(row=6, column=0, padx=10, pady=10)
        self.cep_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.cep_entry.grid(row=6, column=1, padx=10, pady=10)
        
        # Bairro
        self.bairro_label = ct.CTkLabel(self.form_cadastro, text="Bairro:")
        self.bairro_label.grid(row=7, column=0, padx=10, pady=10)
        self.bairro_entry = ct.CTkEntry(self.form_cadastro, width=200)
        self.bairro_entry.grid(row=7, column=1, padx=10, pady=10)
        
        # Botões de Enviar e Sair
        self.submit_button = ct.CTkButton(self.form_cadastro, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=8, column=0, padx=10, pady=10)
        self.exit_button = ct.CTkButton(self.form_cadastro, text="Sair", command=self.destroy)
        self.exit_button.grid(row=8, column=1, padx=10, pady=10)

    
        # Função para criar o formulário de consulta e exibir os dados nas entradas
    
    
    # Função para criar o formulário de consulta
    def create_form_consulta(self):
        self.form_consulta = ct.CTkFrame(self, corner_radius=10)

        # Campos de consulta 

        # Nome
        self.name1_label = ct.CTkLabel(self.form_consulta, text="Nome:")
        self.name1_label.grid(row=0, column=0, pady=10)
        self.name1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.name1_entry.grid(row=0, column=1, pady=10)
        self.name1_entry.bind("<Return>", lambda event: self.auto_fill_form('nome'))

        # RG
        self.rg1_label = ct.CTkLabel(self.form_consulta, text="RG:")
        self.rg1_label.grid(row=1, column=0, padx=10, pady=10)
        self.rg1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.rg1_entry.grid(row=1, column=1, padx=10, pady=10)

        # CPF
        self.cpf1_label = ct.CTkLabel(self.form_consulta, text="CPF:")
        self.cpf1_label.grid(row=2, column=0, padx=10, pady=10)
        self.cpf1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.cpf1_entry.grid(row=2, column=1, padx=10, pady=10)
        self.cpf1_entry.bind("<Return>", lambda event: self.auto_fill_form('cpf'))

        # Email
        self.email1_label = ct.CTkLabel(self.form_consulta, text="Email:")
        self.email1_label.grid(row=3, column=0, padx=10, pady=10)
        self.email1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.email1_entry.grid(row=3, column=1, padx=10, pady=10)

        # Telefone
        self.telefone1_label = ct.CTkLabel(self.form_consulta, text="Telefone:")
        self.telefone1_label.grid(row=4, column=0, padx=10, pady=10)
        self.telefone1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.telefone1_entry.grid(row=4, column=1, padx=10, pady=10)

        # Endereço
        self.endereco1_label = ct.CTkLabel(self.form_consulta, text="Endereço:")
        self.endereco1_label.grid(row=5, column=0, padx=10, pady=10)
        self.endereco1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.endereco1_entry.grid(row=5, column=1, padx=10, pady=10)

        # CEP
        self.cep1_label = ct.CTkLabel(self.form_consulta, text="CEP:")
        self.cep1_label.grid(row=6, column=0, padx=10, pady=10)
        self.cep1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.cep1_entry.grid(row=6, column=1, padx=10, pady=10)

        # Bairro
        self.bairro1_label = ct.CTkLabel(self.form_consulta, text="Bairro:")
        self.bairro1_label.grid(row=7, column=0, padx=10, pady=10)
        self.bairro1_entry = ct.CTkEntry(self.form_consulta, width=200)
        self.bairro1_entry.grid(row=7, column=1, padx=10, pady=10)

    # Função para preencher automaticamente o formulário
    def auto_fill_form(self, field):
        conn = connect_db()
        if conn is None:
            return

        try:
            cursor = conn.cursor()

            # Captura os valores dos campos de entrada
            nome = self.consulta_nome.get()
            cpf = self.consulta_cpf.get()

            # Executa a consulta com base no campo CPF ou Nome
            if field == 'cpf' and cpf:
                query = "SELECT nome, rg, cpf, email, telefone, endereco, cep, bairro FROM clientes WHERE cpf = %s"
                cursor.execute(query, (cpf,))
            elif field == 'nome' and nome:
                query = "SELECT nome, rg, cpf, email, telefone, endereco, cep, bairro FROM clientes WHERE nome ILIKE %s"
                cursor.execute(query, (f"%{nome}%",))
            else:
                return

            result = cursor.fetchone()

            # Se encontrar resultado, preenche os campos
            if result:
                self.name1_entry.delete(0, "end")
                self.name1_entry.insert(0, result[0])

                self.rg1_entry.delete(0, "end")
                self.rg1_entry.insert(0, result[1])

                self.cpf1_entry.delete(0, "end")
                self.cpf1_entry.insert(0, result[2])

                self.email1_entry.delete(0, "end")
                self.email1_entry.insert(0, result[3])

                self.telefone1_entry.delete(0, "end")
                self.telefone1_entry.insert(0, result[4])

                self.endereco1_entry.delete(0, "end")
                self.endereco1_entry.insert(0, result[5])

                self.cep1_entry.delete(0, "end")
                self.cep1_entry.insert(0, result[6])

                self.bairro1_entry.delete(0, "end")
                self.bairro1_entry.insert(0, result[7])

        except Exception as e:
            print(f"Erro ao preencher formulário: {e}")
        finally:
            cursor.close()
            conn.close()

        


    # Função para alternar entre formulários
    def show_form(self, form_name):
        # Esconder todos os formulários
        self.form_cadastro.pack_forget()
        self.form_consulta.pack_forget()
        # self.form_agenda.pack_forget()

        # Mostrar o formulário selecionado
        if form_name == "cadastro":
            self.form_cadastro.pack(fill="both", padx=10, pady=10)
        elif form_name == "consulta":
            self.form_consulta.pack(fill="both", padx=10, pady=10)
      

     # Função para validar o campo RG e CPF usando uma expressão regular
    def validate_entry(self, input_value, max_length):
        # Verifica se o valor é numérico e se não excede o limite de caracteres
        if input_value.isdigit() and len(input_value) <= int(max_length):
            return True
        elif input_value == "":  # Permite apagar (deixar o campo vazio)
            return True
        else:
            return False
    
    # Função para validar CPF sem usar API
    def validate_cpf(self, cpf):
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se o CPF possui 11 dígitos
        if len(cpf) != 11 or not cpf.isdigit():
            return False
        
        # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
        if cpf == cpf[0] * len(cpf):
            return False

        # Cálculo do primeiro dígito verificador
        total = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (total * 10) % 11
        if primeiro_digito == 10:
            primeiro_digito = 0

        # Cálculo do segundo dígito verificador
        total = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (total * 10) % 11
        if segundo_digito == 10:
            segundo_digito = 0

        # Verifica se os dígitos verificadores estão corretos
        return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

    # Função para enviar o formulário
    def submit_form(self):
        conn = connect_db()
        if conn is None:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
            return

        try:
            cursor = conn.cursor()

            # Pegando os valores dos campos
            nome = self.name_entry.get()
            rg = self.rg_entry.get()
            cpf = self.cpf_entry.get()
            email = self.email_entry.get()
            telefone = self.telefone_entry.get()
            endereco = self.endereco_entry.get()
            cep = self.cep_entry.get()
            bairro = self.bairro_entry.get()

            # Validação do CPF
            if not self.validate_cpf(cpf):
                messagebox.showerror("Erro", "CPF inválido.")
                return

            # Inserindo os dados no banco de dados
            query = """
                INSERT INTO clientes (nome, rg, cpf, email, telefone, endereco, cep, bairro)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nome, rg, cpf, email, telefone, endereco, cep, bairro))
            conn.commit()

            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
        finally:
            cursor.close()
            conn.close()




# Inicializa o aplicativo
if __name__ == "__main__":
    app = App()
    app.mainloop()
