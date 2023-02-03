'''
Defines a class, Neuron472455509, of neurons from Allen Brain Institute's model 472455509

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472455509:
    def __init__(self, name="Neuron472455509", x=0, y=0, z=0):
        '''Instantiate Neuron472455509.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472455509_instance is used instead
        '''
                
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg3-Cre_Ai14_GSL_-172530.03.01.01_475124422_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon

        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472455509_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 76.33
            sec.e_pas = -86.5537134806
        
        for sec in self.axon:
            sec.cm = 1.78
            sec.g_pas = 0.000777291891028
        for sec in self.dend:
            sec.cm = 1.78
            sec.g_pas = 6.97005358743e-07
        for sec in self.soma:
            sec.cm = 1.78
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 4.40134e-05
            sec.gbar_NaV = 0.0845222
            sec.gbar_Kd = 7.1396e-06
            sec.gbar_Kv2like = 8.54077e-05
            sec.gbar_Kv3_1 = 0.144688
            sec.gbar_K_T = 4.6547e-06
            sec.gbar_Im_v2 = 0.0194883
            sec.gbar_SK = 0.00891534
            sec.gbar_Ca_HVA = 0.000277947
            sec.gbar_Ca_LVA = 0.00973987
            sec.gamma_CaDynamics = 0.000159404
            sec.decay_CaDynamics = 985.297
            sec.g_pas = 2.59303e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

