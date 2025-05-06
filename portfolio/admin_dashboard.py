from django.contrib.admin.sites import AdminSite

class PortfolioAdminSite(AdminSite):
    site_header = 'Administração do Portfólio'
    site_title = 'Painel Administrativo'
    index_title = 'Bem-vinda ao Painel de Gerenciamento'
    
    def get_app_list(self, request):
        """
        Método sobrescrito para personalizar a ordem e agrupamento dos modelos no admin
        """
        app_list = super().get_app_list(request)
        
        # Criamos uma ordem personalizada para os nossos modelos
        custom_ordering = {
            'Projeto': 1,
            'Certificado': 2,
            'Experiencia': 3,
            'Educacao': 4,
            'HabilidadeTecnica': 5,
            'SoftSkill': 6,
            'Idioma': 7,
            'InformacaoPessoal': 8,
        }
        
        # Organizamos os apps e modelos conforme nossa preferência
        for app in app_list:
            if app['app_label'] == 'portfolio':
                app['name'] = 'Gerenciamento de Portfólio'
                
                # Ordenamos os modelos
                app['models'].sort(key=lambda x: custom_ordering.get(x['object_name'], 99))
                
                # Renomeamos os modelos para nomes mais amigáveis
                model_names = {
                    'Projeto': 'Projetos',
                    'Certificado': 'Certificados',
                    'Experiencia': 'Experiências',
                    'Educacao': 'Formação Acadêmica',
                    'HabilidadeTecnica': 'Habilidades Técnicas',
                    'SoftSkill': 'Soft Skills',
                    'Idioma': 'Idiomas',
                    'InformacaoPessoal': 'Informações Pessoais',
                }
                
                for model in app['models']:
                    if model['object_name'] in model_names:
                        model['name'] = model_names[model['object_name']]
            
            elif app['app_label'] == 'auth':
                app['name'] = 'Autenticação e Permissões'
                
                # Renomeamos os modelos de autenticação
                for model in app['models']:
                    if model['object_name'] == 'User':
                        model['name'] = 'Usuários do Sistema'
                    elif model['object_name'] == 'Group':
                        model['name'] = 'Grupos de Permissão'
        
        return app_list
        
# Instância personalizada do admin site
portfolio_admin_site = PortfolioAdminSite(name='portfolio_admin')