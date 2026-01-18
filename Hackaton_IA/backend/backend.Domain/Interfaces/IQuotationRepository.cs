namespace backend.Domain.Interfaces
{
    public interface IQuotationRepository
    {
        Task<Quotation> GetQuotationAsync(string currencyFrom, string currencyTo);
    }
}