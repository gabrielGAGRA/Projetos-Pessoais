namespace backend.Domain.Entities
{
    public class Quotation
    {
        public string CurrencyFrom { get; set; }
        public string CurrencyTo { get; set; }
        public decimal Rate { get; set; }
        public DateTime Date { get; set; }
    }
}