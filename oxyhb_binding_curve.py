class OxyHbBindingCurve:
    def __init__(self, pco2_mmhg, two_three_dpg_M, temp_c=37.0, ph=7.4):
        """
        Instantiates a new instance of a binding curve object to be calculated
        using the given parameters. Also, it defines a number of constants
        given in the table.

        Parameters
        ----------
        ph : float
            Intracellular pH

        pco2_mmhg : float
            Partial pressure of CO2 in mmHg

        two_three_dpg : float
            Concentration of 2,3-DPG in M.

        temp_c : float
            Temperature in celsius.
        """

        self.k2 = 2.4e-5
        self.k2dd = 1.0e-6
        self.k3 = 2.4e-5
        self.k3dd = 5.0e-6
        self.k4dd = 6.77e11
        self.k5dd = 7.2e-8
        self.k6dd = 8.4e-9
        self.kd = 1200.0
        self.n = 2.7
        self.ideal_gas_const = 62.36   # (L*mmHg) / (mol*K)

        self.ph = ph
        self.pco2_mmhg = pco2_mmhg
        self.two_three_dpg = two_three_dpg_M
        self.temp_c = temp_c

        self.h_plus_M = 10**(-ph)
        self.co2_M = pco2_mmhg / self.ideal_gas_const / temp_c

    @property
    def n1(self):
        return -6.775 + 2.0372*self.ph - 0.1235*self.ph**2
    
    @property
    def n2(self):
        return -0.008765 + 0.00086*self.pco2_mmhg + 6.3e-7*self.pco2_mmhg**2
    
    @property
    def n3(self):
        return 0.2583 + 28.6978*self.two_three_dpg - 917.69*self.two_three_dpg**2
    
    @property 
    def n4(self):
        return 1.6914 + 0.0618*self.temp + 0.00048*self.temp_c**2

    @property
    def k_hbo2(self):
        pass

    def __str__(self):
        return f"pco2_mmhg={self.pco2_mmhg} two_three_dpg_M={self.two_three_dpg} temp_c={self.temp_c} ph={self.ph}"
