class OxyHbBindingCurve:
    def __init__(self, pco2_mmhg, two_three_dpg_M, temp_c=37.0, ph=7.4):
        """
        Instantiates a new instance of a binding curve object to be calculated
        using the given parameters.

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

        self.ph = ph
        self.pco2_mmhg = pco2_mmhg
        self.two_three_dpg = two_three_dpg_M
        self.temp_c = temp_c

    @property
    def n1(self):
        return -6.775 + 2.0372*self.ph - 0.1235*self.ph**2
    
    def __str__(self):
        return f"pco2_mmhg={self.pco2_mmhg} two_three_dpg_M={self.two_three_dpg} temp_c={self.temp_c} ph={self.ph}"
